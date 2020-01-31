import turtle
from antlr4 import *
from Java8Parser import Java8Parser
from Java8Lexer import Java8Lexer

def init_turtle():
    window = turtle.Screen()
    window.screensize(5000, 5000)