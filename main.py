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


def md5_hash(str):
    return hashlib.md5(str.encode("utf-8")).hexdigest()


def fill_icon(hash, palette):
    """
        Fills the icon using a hashed string and a given palette.
    """
    for c in range(0, 18):
        pass


def generate_img():
    pass


def main():
    u = input("String: ")
    p = input("Which palette? (ocean, sunset): ").lower()
    if p in palettes:
        n = int(input("Number of colors (1-4): "))
        u_hash = md5_hash(u)
        print(u_hash)
        fill_icon(u_hash, palettes[p])
        for row in icon:
            print(row)
        generate_img()
    else:
        raise Exception("palette not in palettes")


if __name__ == "__main__":
    main()
