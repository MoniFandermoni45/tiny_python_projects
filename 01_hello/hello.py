#!/usr/bin/env python3
'''
Author:  Piotr Szajewski <szajewskip7@gmail.com>
Purpose: Say hello
'''


import argparse


# ---------------------------------------------------------------------------
def get_args():
    '''Get the command-line arguments'''

    description = "Program that says hello tho the passed name"

    parser = argparse.ArgumentParser(
        description=description
    )  # some description for the parser
    # parser.add_argument('name', help='Name to greet')
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    # we ask parser to parse any arguments passed to the program
    return parser.parse_args()


# ---------------------------------------------------------------------------
def main():
    '''Make a jazz noise here'''

    args = get_args()

    print("Hello, " + args.name + "!")


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
