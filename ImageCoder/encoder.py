from pathlib import Path
from sys import exit
from PIL import Image
from ImageCoder import TERMINATION


def encode(in_file: str, message: str) -> None:
    in_file = Path(in_file)
    try:
        with Image.open(in_file) as image:
            out_file = in_file.parent.joinpath(f"{in_file.stem}_encoded{in_file.suffix}")
            encode_message(message, image)
            image.save(out_file)
    except FileNotFoundError:
        print("File not found")
        exit(1)


def encode_message(msg, image) -> None:
    width, height = image.size
    msg = msg_to_bin(msg)
    msg_length = len(msg)

    if msg_length > width * height:
        print("Cannot fit message in the provided image. Provide bigger image or shorter message.")
        exit(1)

    counter = 0
    for x in range(width):
        if counter >= msg_length: break
        for y in range(height):
            if counter >= msg_length: break
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if counter >= msg_length: break
                pixel[i] = change_bit(pixel[i], int(msg[counter]))
                counter += 1
            image.putpixel((x, y), tuple(pixel))


def change_bit(number: int, last_bit_value: int) -> int:
    return (number & ~1) | last_bit_value


def msg_to_bin(message: str) -> str:
    message += TERMINATION
    return "".join(format(ord(char), "08b") for char in message)
