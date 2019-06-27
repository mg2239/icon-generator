import hashlib
from PIL import ImageDraw, Image, ImageColor

palette = ["#DDE5FF", "#9BB2FF", "#7A99FF", "#597FFF"]
icon = [
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
    ["#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000", "#ff0000"],
]


def md5_hash(str):
    return hashlib.md5(str.encode("utf-8")).hexdigest()


def fill_icon(hash):
    for c in range(0, 18):
        pass


def generate_img():
    pass


def main():
    u = input("String: ")
    n = int(input("Number of colors (1-4): "))
    u_hash = md5_hash(u)
    print(u_hash)
    fill_icon(u_hash)
    for row in icon:
        print(row)
    generate_img()


if __name__ == "__main__":
    main()
