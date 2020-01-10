# Generated from C:/Users/jhons/PycharmProjects/project/grammar\Python3.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Python3Parser import Python3Parser
else:
    from Python3Parser import Python3Parser

# This class defines a complete generic visitor for a parse tree produced by Python3Parser.

class Python3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Python3Parser#inicio.
    def visitInicio(self, ctx:Python3Parser.InicioContext):
        return self.visitChildren(ctx)



del Python3Parser