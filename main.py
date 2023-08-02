#!/usr/bin/env python3

import argparse
from ImageCoder import encoder, decoder


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encode or decode message.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decode', action='store_true', help='Decode the input file into string.')
    group.add_argument('-e', '--encode', action='store_true', help='Encode the input string into file.')
    parser.add_argument('filepath', type=str, help='Image filepath.')

    parser.add_argument('message', type=str, nargs='?', help='Message to be hidden (for encoding).')

    args = parser.parse_args()

    if args.decode and args.encode:
        print("Error: Please select either encode or decode, not both.")
        exit(1)

    if args.encode:
        encoder.encode(args.filepath, args.message)
    elif args.decode:
        print(decoder.decode(args.filepath))
    else:
        print("Error: Please select either encode or decode.")
