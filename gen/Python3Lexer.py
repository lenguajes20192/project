# Generated from C:/Users/jhons/PycharmProjects/project/grammar\Python3.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\6\4\24\n\4\r\4\16\4\25\3\5\6\5\31\n")
        buf.write("\5\r\5\16\5\32\3\5\3\5\2\2\6\3\3\5\4\7\5\t\6\3\2\4\4\2")
        buf.write("C\\c|\5\2\13\f\17\17\"\"\2\37\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\20\3\2\2\2\7\23")
        buf.write("\3\2\2\2\t\30\3\2\2\2\13\f\7j\2\2\f\r\7q\2\2\r\16\7n\2")
        buf.write("\2\16\17\7c\2\2\17\4\3\2\2\2\20\21\7.\2\2\21\6\3\2\2\2")
        buf.write("\22\24\t\2\2\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\b\3\2\2\2\27\31\t\3\2\2\30\27\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\34\3")
        buf.write("\2\2\2\34\35\b\5\2\2\35\n\3\2\2\2\5\2\25\32\3\b\2\2")
        return buf.getvalue()


class Python3Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    ESP = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hola'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "ESP" ]

    ruleNames = [ "T__0", "T__1", "ID", "ESP" ]

    grammarFileName = "Python3.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


