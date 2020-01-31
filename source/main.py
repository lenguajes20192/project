from antlr4 import *
from Java8Parser import Java8Parser
from Java8Lexer import Java8Lexer


def init():
    file_path: "input.txt"

    lexer = Java8Lexer(FileStream(file_path))

    tokens = CommonTokenStream(lexer)
    parser = Java8Parser(tokens)
    tree = parser.literal()
    walker = ParseTreeWalker()

