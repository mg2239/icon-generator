import hashlib
from PIL import ImageDraw, Image, ImageColor

palettes = {
    "ocean": ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"],
    "sunset": ["#FFE0BA", "#FFB978", "#FF898B", "#DB8CD2"],
}
icon = [
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
    ["#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555", "#ff5555"],
]


def md5_hash(s):
    """Hashes string using MD5 hash function."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()

def hex_to_dec(n):
    """Converts hexadecimal number to decimal."""
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
    pass


def main():
    username = input("String: ")
    palette = input("Which palette? (ocean, sunset): ").lower()
    assert palette in palettes
    num_colors = int(input("Number of colors (1-4): "))
    assert num_colors > 0 and num_colors < 5
    user_hash = md5_hash(username)
    print(user_hash)
    fill_icon(user_hash, num_colors, palettes[palette])
    for row in icon:
        print(row)
    generate_img()


if __name__ == "__main__":
    main()
