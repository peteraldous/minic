import sys

from minic_lexer import MiniCLexer
from minic_parser import MiniCParser
from minic_ast import *


def main():
    lexer = MiniCLexer()
    parser = MiniCParser()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "example.mc"

    with open(filename, "r", encoding="utf8") as program:
        text = "\n".join(program.readlines())
        funs = parser.parse(lexer.tokenize(text))
        print("\n\n".join(map(str, funs)))


if __name__ == "__main__":
    main()
