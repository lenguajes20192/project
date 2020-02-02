from antlr4 import *
from RubyParser import RubyParser
from RubyLexer import RubyLexer
from myListener import myListener


def init():
    file_path = "2.txt"

    lexer = RubyLexer(FileStream(file_path))

    tokens = CommonTokenStream(lexer)
    parser = RubyParser(tokens)
    tree = parser.prog()
    walker = ParseTreeWalker()
    walker.walk(myListener(), tree)

init()

