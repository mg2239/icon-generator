import hashlib
from PIL import ImageDraw, Image, ImageColor

palettes = {
    "ocean": ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"],
    "sunset": ["#FFE0BA", "#FFB978", "#FF898B", "#DB8CD2"],
    "caterpillar": ["#E9FFCC", "#A8FFAB", "#7FF0C3", "#7FD5C3"],
}

icon = [
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
]


def get_palettes():
    """ Returns all possible palettes in string format. """
    acc = ""
    for p in palettes:
        acc += p + " "
    return acc.strip()


def md5_hash(s):
    """ 
        Returns a hashed string s using MD5 hash function. 

        Parameters:
        s: An unhashed string.

    """
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def hex_to_dec(n):
    """ 
        Returns a number n converted from decimal to hexadecimal. 

        Parameters:
        n: A number in decimal format.

    """
    return int(n, 16)


def fill_icon(hash_str, num, palette):
    """
        Fills the icon using a hashed string and a given palette.
        
        Parameters:
        hash_str: A hashed string.
        num: The number of colors to use.
        palette: A list containing four hex colors.

    """
    row = 0
    col = 0
    for c in range(0, 18):
        assert row < 6 and col < 3
        color_index = hex_to_dec(hash_str[c]) % num
        color = palette[color_index]
        icon[row][col] = icon[row][5 - col] = color
        if col == 2:
            row += 1
            col = 0
        else:
            col += 1


def generate_img():
    """ Generates an image based on the colors in icon, and saves the resulting image. """
    img_size = 600
    img = Image.new("RGB", (img_size, img_size))
    step_size = img_size / 6
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
    img.save("icon.png", format="PNG")


def main():
    username = input("String: ")
    palette = input("Which palette? (" + get_palettes() + "): ").lower()
    assert palette in palettes
    num_colors = int(input("Number of colors (1-4): "))
    assert num_colors > 0 and num_colors < 5
    user_hash = md5_hash(username)
    fill_icon(user_hash, num_colors, palettes[palette])
    generate_img()


if __name__ == "__main__":
    main()
