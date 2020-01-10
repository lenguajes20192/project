# Generated from C:/Users/jhons/PycharmProjects/project/grammar\Python3.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\16\4\2\t\2\3\2\3\2\3\2\3\2\7\2\t\n\2\f\2\16\2\f\13\2")
        buf.write("\3\2\2\2\3\2\2\2\2\r\2\4\3\2\2\2\4\5\7\3\2\2\5\n\7\5\2")
        buf.write("\2\6\7\7\4\2\2\7\t\7\5\2\2\b\6\3\2\2\2\t\f\3\2\2\2\n\b")
        buf.write("\3\2\2\2\n\13\3\2\2\2\13\3\3\2\2\2\f\n\3\2\2\2\3\n")
        return buf.getvalue()


class Python3Parser ( Parser ):

    grammarFileName = "Python3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "ESP" ]

    RULE_inicio = 0

    ruleNames =  [ "inicio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    ESP=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Python3Parser.ID)
            else:
                return self.getToken(Python3Parser.ID, i)

        def getRuleIndex(self):
            return Python3Parser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = Python3Parser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(Python3Parser.T__0)
            self.state = 3
            self.match(Python3Parser.ID)
            self.state = 8
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Python3Parser.T__1:
                self.state = 4
                self.match(Python3Parser.T__1)
                self.state = 5
                self.match(Python3Parser.ID)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





