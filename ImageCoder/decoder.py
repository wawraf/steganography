from pathlib import Path
from sys import exit
from PIL import Image
from ImageCoder import TERMINATION

t = "".join([format(ord(char), '08b') for char in TERMINATION])


def decode(in_file: str) -> str:
    in_file = Path(in_file)
    try:
        with Image.open(in_file) as image:
            return decode_message(image)
    except FileNotFoundError:
        print("File not found")
        exit(1)


def decode_message(image: Image) -> str:
    width, height = image.size
    msg = ""

    for x in range(width):
        if check_null(msg): break
        for y in range(height):
            if check_null(msg): break
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if check_null(msg): break
                msg += get_bit(pixel[i])
    return bin_to_msg(msg[:-len(t)])


def check_null(msg: str) -> bool:
    return msg[-len(t):] == t and len(msg) % 8 == 0


def get_bit(number: int) -> str:
    return str(number & 1)


def bin_to_msg(binary_str: str) -> str:
    if len(binary_str) % 8 != 0:
        raise ValueError("Invalid binary string length. It should be a multiple of 8.")

    binary_segments = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

    ascii_str = "".join(chr(int(segment, 2)) for segment in binary_segments)

    return ascii_str
