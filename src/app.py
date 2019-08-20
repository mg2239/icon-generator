import hashlib, requests, json, base64
from PIL import ImageDraw, Image, ImageColor, ImageOps
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

palettes = {
    "ocean": ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"],
    "sunset": ["#FFE0BA", "#FFB978", "#FF898B", "#DB8CD2"],
    "dragon": ["#E3FFEE", "#84CFA3", "#57B098", "#308A8F"],
    "sakura": ["#eee6fb", "#dfb0d3", "#d983a6", "#d94773"]
}

icon = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

@app.route("/api/palettes")
def get_palettes():
    """
        Returns all possible palettes, separated by a space.
    """
    acc = ""
    for p in palettes:
        acc += p + " "
    return json.dumps({"success": True, "data": acc.strip()}), 200

@app.route("/api/generate/")
def get_icon():
    """
        Gets icon data from request and returns JSON containing icon"s Imgur link
        or an error.
    """
    username = request.args.get('username')
    palette = request.args.get('palette')
    num_colors = int(request.args.get('num_colors'))
    if palette in palettes and 1 < num_colors < 5:
        user_hash = md5_hash(username)
        fill_icon(user_hash, num_colors, palettes[palette])
        filename = generate_img(username, num_colors, palette)
        imgur_url = get_imgur_url(img_to_b64(filename))
        return json.dumps({"success": True, "data": imgur_url}), 200
    return json.dumps({"success": False, "error": "One or more parameters are invalid."}), 500

def md5_hash(s):
    """ 
        Returns a hashed string s using MD5 hash function. 

        Parameters:
        s: An unhashed string.

    """
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def hex_to_dec(n):
    """ 
        Returns a int n converted from decimal to hexadecimal. 

        Parameters:
        n: An int in decimal format.

    """
    return int(n, 16)


def fill_icon(hash_str, num_colors, palette):
    """
        Fills the icon using a hashed string and a given palette.
        
        Parameters:
        hash_str: A hashed string.
        num_colors: The number of colors to use.
        palette: A list containing four hex colors.

    """
    row = 0
    col = 0
    for c in range(0, 15):
        color_index = hex_to_dec(hash_str[c]) % num_colors
        color = palette[color_index]
        icon[row][col] = icon[row][4 - col] = color
        if col == 2:
            row += 1
            col = 0
        else:
            col += 1


def generate_img(username, num_colors, palette):
    """
        Generates an image based on the colors in icon, and saves the resulting image.
        Returns the file name of the icon.
    
        Parameters:
        username: The username used to create the icon.
        num_colors: The number of colors.
        palette: The palette used to color the icon.

        Preconditions:
        username is a string and contains no whitespace
        num_colors is an int
        palette is a string

    """
    bg_color = palettes[palette][0]
    img_size = 500
    img = Image.new("RGB", (img_size, img_size))
    step_size = img_size / 5
    x = 0
    y = img_size - step_size
    for row_color in icon:
        for hex_color in row_color:
            rgb_color = ImageColor.getrgb(hex_color)
            draw = ImageDraw.Draw(img)
            draw.rectangle(
                [x, y, x + step_size, y + step_size], rgb_color, rgb_color, 0
            )
            if x == img_size - step_size:
                x = 0
                y -= step_size
            else:
                x += step_size
    img = ImageOps.expand(img, 80, bg_color)
    filename = "icon_" + username + "_" + palette + "_" +  str(num_colors) + ".png"
    img.save(filename, format="PNG")
    return filename

def img_to_b64(filename):
    """
        Returns image located at filename encoded as a base64 string.
    """
    with open(filename, "rb") as img_file:
        img_str = str(base64.b64encode(img_file.read()))
    img = img_str[2:len(img_str)-1]
    return img

def get_imgur_url(b64_img):
    """
        Uploads base64 image b64_img to Imgur and returns the link to the upload.
    """
    url = "https://api.imgur.com/3/upload"
    header = {
        "Authorization": "Client-ID " + "e63dea1dd7901ee"
    }
    files = {}
    body = {
        "image": b64_img
    }
    res = requests.request("POST", url, headers=header, data=body, files=files, allow_redirects=False)
    return json.loads(res.text)["data"]["link"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
