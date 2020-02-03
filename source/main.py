import numpy as np
from antlr4 import *
from RubyParser import RubyParser
from RubyLexer import RubyLexer
from myListener import myListener


def init():
    text_arr = np.array(["elsif.txt", "ifelseif.txt", "for.txt"])
    file_path = text_arr[2]


    lexer = RubyLexer(FileStream(file_path))

    tokens = CommonTokenStream(lexer)
    parser = RubyParser(tokens)
    tree = parser.prog()
    walker = ParseTreeWalker()
    walker.walk(myListener(), tree)

init()

