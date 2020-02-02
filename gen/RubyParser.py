# Generated from C:/Users/User/Documents/project/grammar\Ruby.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u033b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u009a\n\3\3\3\3\3\3\3\3\3\7\3\u00a0\n\3\f\3")
        buf.write("\16\3\u00a3\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u00af\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u00d6\n\16\3\17\3\17\5\17\u00da\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00e3\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\7\21\u00eb\n\21\f\21\16\21")
        buf.write("\u00ee\13\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0101")
        buf.write("\n\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u010b")
        buf.write("\n\26\f\26\16\26\u010e\13\26\3\27\3\27\5\27\u0112\n\27")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u0118\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u0120\n\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0129\n\33\3\34\3\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\5\35\u0140\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0158")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0170\n\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\5!\u018f\n!\3\"\3\"\3#\3#\3#\3#\5#\u0197\n#\3$\3$\3")
        buf.write("$\3$\3$\3$\7$\u019f\n$\f$\16$\u01a2\13$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\7\'\u01ae\n\'\f\'\16\'\u01b1\13")
        buf.write("\'\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01be\n)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u01cb\n)\f)\16)\u01ce\13")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01d8\n*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\5+\u01e2\n+\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01ec\n")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01f6\n-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u0200\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\5\62\u0212\n\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u0218\n\62\7\62\u021a\n\62\f\62")
        buf.write("\16\62\u021d\13\62\3\63\3\63\3\63\3\63\5\63\u0223\n\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u022b\n\63\3\63\3")
        buf.write("\63\5\63\u022f\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u024b\n")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\7\64\u0262\n\64\f\64\16\64\u0265\13\64\3\65\3\65\3\65")
        buf.write("\5\65\u026a\n\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0272")
        buf.write("\n\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u027a\n\66\f")
        buf.write("\66\16\66\u027d\13\66\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u028d\n\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\7\67\u029b\n\67\f\67\16\67\u029e\13\67\38\38\38")
        buf.write("\38\38\38\58\u02a6\n8\38\38\38\38\38\38\78\u02ae\n8\f")
        buf.write("8\168\u02b1\138\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\59\u02c8\n9\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\5:\u02d2\n:\3;\3;\3;\5;\u02d7\n;\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\5=\u02f5\n=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\7=\u0312\n=\f=\16=\u0315\13=\3>\3>\3?\3?\3@\3@\3A\3")
        buf.write("A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3G\5G\u032c\nG\3")
        buf.write("G\3G\3G\3G\7G\u0332\nG\fG\16G\u0335\13G\3H\3H\3I\3I\3")
        buf.write("I\2\17\4 *FLPbfjlnx\u008cJ\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\2\f\3\2$)\3\2\31\33\3\2\27\30\3\2\37")
        buf.write("\"\3\2\35\36\4\2--\62\62\3\2./\3\2+,\3\2\60\61\3\2\25")
        buf.write("\26\2\u0370\2\u0092\3\2\2\2\4\u0099\3\2\2\2\6\u00ae\3")
        buf.write("\2\2\2\b\u00b0\3\2\2\2\n\u00b4\3\2\2\2\f\u00b8\3\2\2\2")
        buf.write("\16\u00ba\3\2\2\2\20\u00bc\3\2\2\2\22\u00bf\3\2\2\2\24")
        buf.write("\u00c4\3\2\2\2\26\u00c6\3\2\2\2\30\u00ca\3\2\2\2\32\u00d5")
        buf.write("\3\2\2\2\34\u00d9\3\2\2\2\36\u00e2\3\2\2\2 \u00e4\3\2")
        buf.write("\2\2\"\u00ef\3\2\2\2$\u00f1\3\2\2\2&\u0100\3\2\2\2(\u0102")
        buf.write("\3\2\2\2*\u0104\3\2\2\2,\u0111\3\2\2\2.\u0117\3\2\2\2")
        buf.write("\60\u0119\3\2\2\2\62\u0121\3\2\2\2\64\u0128\3\2\2\2\66")
        buf.write("\u012a\3\2\2\28\u013f\3\2\2\2:\u0157\3\2\2\2<\u016f\3")
        buf.write("\2\2\2>\u0171\3\2\2\2@\u018e\3\2\2\2B\u0190\3\2\2\2D\u0196")
        buf.write("\3\2\2\2F\u0198\3\2\2\2H\u01a3\3\2\2\2J\u01a5\3\2\2\2")
        buf.write("L\u01a7\3\2\2\2N\u01b2\3\2\2\2P\u01bd\3\2\2\2R\u01d7\3")
        buf.write("\2\2\2T\u01e1\3\2\2\2V\u01eb\3\2\2\2X\u01f5\3\2\2\2Z\u01ff")
        buf.write("\3\2\2\2\\\u0201\3\2\2\2^\u0206\3\2\2\2`\u020a\3\2\2\2")
        buf.write("b\u020e\3\2\2\2d\u022e\3\2\2\2f\u024a\3\2\2\2h\u0269\3")
        buf.write("\2\2\2j\u0271\3\2\2\2l\u028c\3\2\2\2n\u02a5\3\2\2\2p\u02c7")
        buf.write("\3\2\2\2r\u02d1\3\2\2\2t\u02d6\3\2\2\2v\u02d8\3\2\2\2")
        buf.write("x\u02f4\3\2\2\2z\u0316\3\2\2\2|\u0318\3\2\2\2~\u031a\3")
        buf.write("\2\2\2\u0080\u031c\3\2\2\2\u0082\u031e\3\2\2\2\u0084\u0320")
        buf.write("\3\2\2\2\u0086\u0322\3\2\2\2\u0088\u0324\3\2\2\2\u008a")
        buf.write("\u0326\3\2\2\2\u008c\u032b\3\2\2\2\u008e\u0336\3\2\2\2")
        buf.write("\u0090\u0338\3\2\2\2\u0092\u0093\5\4\3\2\u0093\3\3\2\2")
        buf.write("\2\u0094\u0095\b\3\1\2\u0095\u0096\5\6\4\2\u0096\u0097")
        buf.write("\5\u008cG\2\u0097\u009a\3\2\2\2\u0098\u009a\5\u008cG\2")
        buf.write("\u0099\u0094\3\2\2\2\u0099\u0098\3\2\2\2\u009a\u00a1\3")
        buf.write("\2\2\2\u009b\u009c\f\4\2\2\u009c\u009d\5\6\4\2\u009d\u009e")
        buf.write("\5\u008cG\2\u009e\u00a0\3\2\2\2\u009f\u009b\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00af\5\26")
        buf.write("\f\2\u00a5\u00af\5\16\b\2\u00a6\u00af\5\20\t\2\u00a7\u00af")
        buf.write("\5:\36\2\u00a8\u00af\5<\37\2\u00a9\u00af\5x=\2\u00aa\u00af")
        buf.write("\5$\23\2\u00ab\u00af\5> \2\u00ac\u00af\5@!\2\u00ad\u00af")
        buf.write("\5\22\n\2\u00ae\u00a4\3\2\2\2\u00ae\u00a5\3\2\2\2\u00ae")
        buf.write("\u00a6\3\2\2\2\u00ae\u00a7\3\2\2\2\u00ae\u00a8\3\2\2\2")
        buf.write("\u00ae\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\7")
        buf.write("\3\2\2\2\u00b0\u00b1\5v<\2\u00b1\u00b2\7#\2\2\u00b2\u00b3")
        buf.write("\5\u0088E\2\u00b3\t\3\2\2\2\u00b4\u00b5\5\u0088E\2\u00b5")
        buf.write("\u00b6\7#\2\2\u00b6\u00b7\5\64\33\2\u00b7\13\3\2\2\2\u00b8")
        buf.write("\u00b9\5\u0088E\2\u00b9\r\3\2\2\2\u00ba\u00bb\5&\24\2")
        buf.write("\u00bb\17\3\2\2\2\u00bc\u00bd\7\7\2\2\u00bd\u00be\5|?")
        buf.write("\2\u00be\21\3\2\2\2\u00bf\u00c0\7\13\2\2\u00c0\u00c1\5")
        buf.write("\u0090I\2\u00c1\u00c2\5\24\13\2\u00c2\u00c3\7\b\2\2\u00c3")
        buf.write("\23\3\2\2\2\u00c4\u00c5\5\4\3\2\u00c5\25\3\2\2\2\u00c6")
        buf.write("\u00c7\5\32\16\2\u00c7\u00c8\5\30\r\2\u00c8\u00c9\7\b")
        buf.write("\2\2\u00c9\27\3\2\2\2\u00ca\u00cb\5\4\3\2\u00cb\31\3\2")
        buf.write("\2\2\u00cc\u00cd\7\t\2\2\u00cd\u00ce\5\34\17\2\u00ce\u00cf")
        buf.write("\5\u0090I\2\u00cf\u00d6\3\2\2\2\u00d0\u00d1\7\t\2\2\u00d1")
        buf.write("\u00d2\5\34\17\2\u00d2\u00d3\5\36\20\2\u00d3\u00d4\5\u0090")
        buf.write("I\2\u00d4\u00d6\3\2\2\2\u00d5\u00cc\3\2\2\2\u00d5\u00d0")
        buf.write("\3\2\2\2\u00d6\33\3\2\2\2\u00d7\u00da\5\u008aF\2\u00d8")
        buf.write("\u00da\5\u0086D\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2")
        buf.write("\2\2\u00da\35\3\2\2\2\u00db\u00dc\7\63\2\2\u00dc\u00e3")
        buf.write("\7\64\2\2\u00dd\u00de\7\63\2\2\u00de\u00df\5 \21\2\u00df")
        buf.write("\u00e0\7\64\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5 \21")
        buf.write("\2\u00e2\u00db\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2\u00e1")
        buf.write("\3\2\2\2\u00e3\37\3\2\2\2\u00e4\u00e5\b\21\1\2\u00e5\u00e6")
        buf.write("\5\"\22\2\u00e6\u00ec\3\2\2\2\u00e7\u00e8\f\3\2\2\u00e8")
        buf.write("\u00e9\7\4\2\2\u00e9\u00eb\5\"\22\2\u00ea\u00e7\3\2\2")
        buf.write("\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed!\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0")
        buf.write("\5\u0086D\2\u00f0#\3\2\2\2\u00f1\u00f2\7\n\2\2\u00f2\u00f3")
        buf.write("\5\64\33\2\u00f3%\3\2\2\2\u00f4\u00f5\5\34\17\2\u00f5")
        buf.write("\u00f6\7\63\2\2\u00f6\u00f7\5(\25\2\u00f7\u00f8\7\64\2")
        buf.write("\2\u00f8\u0101\3\2\2\2\u00f9\u00fa\5\34\17\2\u00fa\u00fb")
        buf.write("\5(\25\2\u00fb\u0101\3\2\2\2\u00fc\u00fd\5\34\17\2\u00fd")
        buf.write("\u00fe\7\63\2\2\u00fe\u00ff\7\64\2\2\u00ff\u0101\3\2\2")
        buf.write("\2\u0100\u00f4\3\2\2\2\u0100\u00f9\3\2\2\2\u0100\u00fc")
        buf.write("\3\2\2\2\u0101\'\3\2\2\2\u0102\u0103\5*\26\2\u0103)\3")
        buf.write("\2\2\2\u0104\u0105\b\26\1\2\u0105\u0106\5,\27\2\u0106")
        buf.write("\u010c\3\2\2\2\u0107\u0108\f\3\2\2\u0108\u0109\7\4\2\2")
        buf.write("\u0109\u010b\5,\27\2\u010a\u0107\3\2\2\2\u010b\u010e\3")
        buf.write("\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d+")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0112\5.\30\2\u0110")
        buf.write("\u0112\5\60\31\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2")
        buf.write("\2\u0112-\3\2\2\2\u0113\u0118\5j\66\2\u0114\u0118\5l\67")
        buf.write("\2\u0115\u0118\5n8\2\u0116\u0118\5f\64\2\u0117\u0113\3")
        buf.write("\2\2\2\u0117\u0114\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118/\3\2\2\2\u0119\u011a\5\u0086D\2\u011a\u011f")
        buf.write("\7#\2\2\u011b\u0120\5j\66\2\u011c\u0120\5l\67\2\u011d")
        buf.write("\u0120\5n8\2\u011e\u0120\5f\64\2\u011f\u011b\3\2\2\2\u011f")
        buf.write("\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120\61\3\2\2\2\u0121\u0122\5&\24\2\u0122\63\3\2\2\2")
        buf.write("\u0123\u0129\5j\66\2\u0124\u0129\5l\67\2\u0125\u0129\5")
        buf.write("n8\2\u0126\u0129\5f\64\2\u0127\u0129\5\f\7\2\u0128\u0123")
        buf.write("\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0125\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129\65\3\2\2\2\u012a")
        buf.write("\u012b\58\35\2\u012b\67\3\2\2\2\u012c\u012d\7\16\2\2\u012d")
        buf.write("\u012e\5H%\2\u012e\u012f\5\u0090I\2\u012f\u0130\5N(\2")
        buf.write("\u0130\u0140\3\2\2\2\u0131\u0132\7\16\2\2\u0132\u0133")
        buf.write("\5H%\2\u0133\u0134\5\u0090I\2\u0134\u0135\5N(\2\u0135")
        buf.write("\u0136\5\u008eH\2\u0136\u0137\5\u0090I\2\u0137\u0138\5")
        buf.write("N(\2\u0138\u0140\3\2\2\2\u0139\u013a\7\16\2\2\u013a\u013b")
        buf.write("\5H%\2\u013b\u013c\5\u0090I\2\u013c\u013d\5N(\2\u013d")
        buf.write("\u013e\58\35\2\u013e\u0140\3\2\2\2\u013f\u012c\3\2\2\2")
        buf.write("\u013f\u0131\3\2\2\2\u013f\u0139\3\2\2\2\u01409\3\2\2")
        buf.write("\2\u0141\u0142\7\f\2\2\u0142\u0143\5H%\2\u0143\u0144\5")
        buf.write("\u0090I\2\u0144\u0145\5N(\2\u0145\u0146\7\b\2\2\u0146")
        buf.write("\u0158\3\2\2\2\u0147\u0148\7\f\2\2\u0148\u0149\5H%\2\u0149")
        buf.write("\u014a\5\u0090I\2\u014a\u014b\5N(\2\u014b\u014c\5\u008e")
        buf.write("H\2\u014c\u014d\5\u0090I\2\u014d\u014e\5N(\2\u014e\u014f")
        buf.write("\7\b\2\2\u014f\u0158\3\2\2\2\u0150\u0151\7\f\2\2\u0151")
        buf.write("\u0152\5H%\2\u0152\u0153\5\u0090I\2\u0153\u0154\5N(\2")
        buf.write("\u0154\u0155\5\66\34\2\u0155\u0156\7\b\2\2\u0156\u0158")
        buf.write("\3\2\2\2\u0157\u0141\3\2\2\2\u0157\u0147\3\2\2\2\u0157")
        buf.write("\u0150\3\2\2\2\u0158;\3\2\2\2\u0159\u015a\7\17\2\2\u015a")
        buf.write("\u015b\5H%\2\u015b\u015c\5\u0090I\2\u015c\u015d\5N(\2")
        buf.write("\u015d\u015e\7\b\2\2\u015e\u0170\3\2\2\2\u015f\u0160\7")
        buf.write("\17\2\2\u0160\u0161\5H%\2\u0161\u0162\5\u0090I\2\u0162")
        buf.write("\u0163\5N(\2\u0163\u0164\5\u008eH\2\u0164\u0165\5\u0090")
        buf.write("I\2\u0165\u0166\5N(\2\u0166\u0167\7\b\2\2\u0167\u0170")
        buf.write("\3\2\2\2\u0168\u0169\7\17\2\2\u0169\u016a\5H%\2\u016a")
        buf.write("\u016b\5\u0090I\2\u016b\u016c\5N(\2\u016c\u016d\5\66\34")
        buf.write("\2\u016d\u016e\7\b\2\2\u016e\u0170\3\2\2\2\u016f\u0159")
        buf.write("\3\2\2\2\u016f\u015f\3\2\2\2\u016f\u0168\3\2\2\2\u0170")
        buf.write("=\3\2\2\2\u0171\u0172\7\20\2\2\u0172\u0173\5H%\2\u0173")
        buf.write("\u0174\7\24\2\2\u0174\u0175\5\u0090I\2\u0175\u0176\5N")
        buf.write("(\2\u0176\u0177\7\b\2\2\u0177?\3\2\2\2\u0178\u0179\7\23")
        buf.write("\2\2\u0179\u017a\7\63\2\2\u017a\u017b\5B\"\2\u017b\u017c")
        buf.write("\7\5\2\2\u017c\u017d\5H%\2\u017d\u017e\7\5\2\2\u017e\u017f")
        buf.write("\5J&\2\u017f\u0180\7\64\2\2\u0180\u0181\5\u0090I\2\u0181")
        buf.write("\u0182\5N(\2\u0182\u0183\7\b\2\2\u0183\u018f\3\2\2\2\u0184")
        buf.write("\u0185\7\23\2\2\u0185\u0186\5B\"\2\u0186\u0187\7\5\2\2")
        buf.write("\u0187\u0188\5H%\2\u0188\u0189\7\5\2\2\u0189\u018a\5J")
        buf.write("&\2\u018a\u018b\5\u0090I\2\u018b\u018c\5N(\2\u018c\u018d")
        buf.write("\7\b\2\2\u018d\u018f\3\2\2\2\u018e\u0178\3\2\2\2\u018e")
        buf.write("\u0184\3\2\2\2\u018fA\3\2\2\2\u0190\u0191\5F$\2\u0191")
        buf.write("C\3\2\2\2\u0192\u0197\5V,\2\u0193\u0197\5X-\2\u0194\u0197")
        buf.write("\5Z.\2\u0195\u0197\5T+\2\u0196\u0192\3\2\2\2\u0196\u0193")
        buf.write("\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("E\3\2\2\2\u0198\u0199\b$\1\2\u0199\u019a\5D#\2\u019a\u01a0")
        buf.write("\3\2\2\2\u019b\u019c\f\4\2\2\u019c\u019d\7\4\2\2\u019d")
        buf.write("\u019f\5D#\2\u019e\u019b\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1G\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\5p9\2\u01a4I\3\2\2\2\u01a5")
        buf.write("\u01a6\5L\'\2\u01a6K\3\2\2\2\u01a7\u01a8\b\'\1\2\u01a8")
        buf.write("\u01a9\5D#\2\u01a9\u01af\3\2\2\2\u01aa\u01ab\f\4\2\2\u01ab")
        buf.write("\u01ac\7\4\2\2\u01ac\u01ae\5D#\2\u01ad\u01aa\3\2\2\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0M\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\5P)\2")
        buf.write("\u01b3O\3\2\2\2\u01b4\u01b5\b)\1\2\u01b5\u01b6\5\6\4\2")
        buf.write("\u01b6\u01b7\5\u008cG\2\u01b7\u01be\3\2\2\2\u01b8\u01b9")
        buf.write("\7\21\2\2\u01b9\u01be\5\u008cG\2\u01ba\u01bb\5z>\2\u01bb")
        buf.write("\u01bc\5\u008cG\2\u01bc\u01be\3\2\2\2\u01bd\u01b4\3\2")
        buf.write("\2\2\u01bd\u01b8\3\2\2\2\u01bd\u01ba\3\2\2\2\u01be\u01cc")
        buf.write("\3\2\2\2\u01bf\u01c0\f\5\2\2\u01c0\u01c1\5\6\4\2\u01c1")
        buf.write("\u01c2\5\u008cG\2\u01c2\u01cb\3\2\2\2\u01c3\u01c4\f\4")
        buf.write("\2\2\u01c4\u01c5\7\21\2\2\u01c5\u01cb\5\u008cG\2\u01c6")
        buf.write("\u01c7\f\3\2\2\u01c7\u01c8\5z>\2\u01c8\u01c9\5\u008cG")
        buf.write("\2\u01c9\u01cb\3\2\2\2\u01ca\u01bf\3\2\2\2\u01ca\u01c3")
        buf.write("\3\2\2\2\u01ca\u01c6\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cdQ\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d0\5v<\2\u01d0\u01d1\7#\2\2\u01d1")
        buf.write("\u01d2\5x=\2\u01d2\u01d8\3\2\2\2\u01d3\u01d4\5v<\2\u01d4")
        buf.write("\u01d5\t\2\2\2\u01d5\u01d6\5x=\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01cf\3\2\2\2\u01d7\u01d3\3\2\2\2\u01d8S\3\2\2\2\u01d9")
        buf.write("\u01da\5v<\2\u01da\u01db\7#\2\2\u01db\u01dc\5f\64\2\u01dc")
        buf.write("\u01e2\3\2\2\2\u01dd\u01de\5v<\2\u01de\u01df\t\2\2\2\u01df")
        buf.write("\u01e0\5f\64\2\u01e0\u01e2\3\2\2\2\u01e1\u01d9\3\2\2\2")
        buf.write("\u01e1\u01dd\3\2\2\2\u01e2U\3\2\2\2\u01e3\u01e4\5v<\2")
        buf.write("\u01e4\u01e5\7#\2\2\u01e5\u01e6\5j\66\2\u01e6\u01ec\3")
        buf.write("\2\2\2\u01e7\u01e8\5v<\2\u01e8\u01e9\t\2\2\2\u01e9\u01ea")
        buf.write("\5j\66\2\u01ea\u01ec\3\2\2\2\u01eb\u01e3\3\2\2\2\u01eb")
        buf.write("\u01e7\3\2\2\2\u01ecW\3\2\2\2\u01ed\u01ee\5v<\2\u01ee")
        buf.write("\u01ef\7#\2\2\u01ef\u01f0\5l\67\2\u01f0\u01f6\3\2\2\2")
        buf.write("\u01f1\u01f2\5v<\2\u01f2\u01f3\t\2\2\2\u01f3\u01f4\5l")
        buf.write("\67\2\u01f4\u01f6\3\2\2\2\u01f5\u01ed\3\2\2\2\u01f5\u01f1")
        buf.write("\3\2\2\2\u01f6Y\3\2\2\2\u01f7\u01f8\5v<\2\u01f8\u01f9")
        buf.write("\7#\2\2\u01f9\u01fa\5n8\2\u01fa\u0200\3\2\2\2\u01fb\u01fc")
        buf.write("\5v<\2\u01fc\u01fd\7$\2\2\u01fd\u01fe\5n8\2\u01fe\u0200")
        buf.write("\3\2\2\2\u01ff\u01f7\3\2\2\2\u01ff\u01fb\3\2\2\2\u0200")
        buf.write("[\3\2\2\2\u0201\u0202\5v<\2\u0202\u0203\7#\2\2\u0203\u0204")
        buf.write("\7\65\2\2\u0204\u0205\7\66\2\2\u0205]\3\2\2\2\u0206\u0207")
        buf.write("\5d\63\2\u0207\u0208\7#\2\2\u0208\u0209\5\64\33\2\u0209")
        buf.write("_\3\2\2\2\u020a\u020b\7\65\2\2\u020b\u020c\5b\62\2\u020c")
        buf.write("\u020d\7\66\2\2\u020da\3\2\2\2\u020e\u0211\b\62\1\2\u020f")
        buf.write("\u0212\5j\66\2\u0210\u0212\5f\64\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0210\3\2\2\2\u0212\u021b\3\2\2\2\u0213\u0214\f")
        buf.write("\3\2\2\u0214\u0217\7\4\2\2\u0215\u0218\5j\66\2\u0216\u0218")
        buf.write("\5f\64\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u0213\3\2\2\2\u021a\u021d\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021cc\3\2\2")
        buf.write("\2\u021d\u021b\3\2\2\2\u021e\u021f\5\u0086D\2\u021f\u0222")
        buf.write("\7\65\2\2\u0220\u0223\5j\66\2\u0221\u0223\5f\64\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0221\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0225\7\66\2\2\u0225\u022f\3\2\2\2\u0226\u0227")
        buf.write("\5\u0088E\2\u0227\u022a\7\65\2\2\u0228\u022b\5j\66\2\u0229")
        buf.write("\u022b\5f\64\2\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022d\7\66\2\2\u022d\u022f")
        buf.write("\3\2\2\2\u022e\u021e\3\2\2\2\u022e\u0226\3\2\2\2\u022f")
        buf.write("e\3\2\2\2\u0230\u0231\b\64\1\2\u0231\u0232\5j\66\2\u0232")
        buf.write("\u0233\t\3\2\2\u0233\u0234\5f\64\17\u0234\u024b\3\2\2")
        buf.write("\2\u0235\u0236\5l\67\2\u0236\u0237\t\3\2\2\u0237\u0238")
        buf.write("\5f\64\r\u0238\u024b\3\2\2\2\u0239\u023a\5n8\2\u023a\u023b")
        buf.write("\7\31\2\2\u023b\u023c\5f\64\n\u023c\u024b\3\2\2\2\u023d")
        buf.write("\u023e\5j\66\2\u023e\u023f\t\4\2\2\u023f\u0240\5f\64\b")
        buf.write("\u0240\u024b\3\2\2\2\u0241\u0242\5l\67\2\u0242\u0243\t")
        buf.write("\4\2\2\u0243\u0244\5f\64\6\u0244\u024b\3\2\2\2\u0245\u0246")
        buf.write("\7\63\2\2\u0246\u0247\5f\64\2\u0247\u0248\7\64\2\2\u0248")
        buf.write("\u024b\3\2\2\2\u0249\u024b\5h\65\2\u024a\u0230\3\2\2\2")
        buf.write("\u024a\u0235\3\2\2\2\u024a\u0239\3\2\2\2\u024a\u023d\3")
        buf.write("\2\2\2\u024a\u0241\3\2\2\2\u024a\u0245\3\2\2\2\u024a\u0249")
        buf.write("\3\2\2\2\u024b\u0263\3\2\2\2\u024c\u024d\f\f\2\2\u024d")
        buf.write("\u024e\t\3\2\2\u024e\u0262\5f\64\r\u024f\u0250\f\5\2\2")
        buf.write("\u0250\u0251\t\4\2\2\u0251\u0262\5f\64\6\u0252\u0253\f")
        buf.write("\20\2\2\u0253\u0254\t\3\2\2\u0254\u0262\5j\66\2\u0255")
        buf.write("\u0256\f\16\2\2\u0256\u0257\t\3\2\2\u0257\u0262\5l\67")
        buf.write("\2\u0258\u0259\f\13\2\2\u0259\u025a\7\31\2\2\u025a\u0262")
        buf.write("\5n8\2\u025b\u025c\f\t\2\2\u025c\u025d\t\4\2\2\u025d\u0262")
        buf.write("\5j\66\2\u025e\u025f\f\7\2\2\u025f\u0260\t\4\2\2\u0260")
        buf.write("\u0262\5l\67\2\u0261\u024c\3\2\2\2\u0261\u024f\3\2\2\2")
        buf.write("\u0261\u0252\3\2\2\2\u0261\u0255\3\2\2\2\u0261\u0258\3")
        buf.write("\2\2\2\u0261\u025b\3\2\2\2\u0261\u025e\3\2\2\2\u0262\u0265")
        buf.write("\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write("g\3\2\2\2\u0265\u0263\3\2\2\2\u0266\u026a\5\u0086D\2\u0267")
        buf.write("\u026a\5\62\32\2\u0268\u026a\5d\63\2\u0269\u0266\3\2\2")
        buf.write("\2\u0269\u0267\3\2\2\2\u0269\u0268\3\2\2\2\u026ai\3\2")
        buf.write("\2\2\u026b\u026c\b\66\1\2\u026c\u026d\7\63\2\2\u026d\u026e")
        buf.write("\5j\66\2\u026e\u026f\7\64\2\2\u026f\u0272\3\2\2\2\u0270")
        buf.write("\u0272\5\u0080A\2\u0271\u026b\3\2\2\2\u0271\u0270\3\2")
        buf.write("\2\2\u0272\u027b\3\2\2\2\u0273\u0274\f\6\2\2\u0274\u0275")
        buf.write("\t\3\2\2\u0275\u027a\5j\66\7\u0276\u0277\f\5\2\2\u0277")
        buf.write("\u0278\t\4\2\2\u0278\u027a\5j\66\6\u0279\u0273\3\2\2\2")
        buf.write("\u0279\u0276\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027b\u027c\3\2\2\2\u027ck\3\2\2\2\u027d\u027b")
        buf.write("\3\2\2\2\u027e\u027f\b\67\1\2\u027f\u0280\5j\66\2\u0280")
        buf.write("\u0281\t\3\2\2\u0281\u0282\5l\67\t\u0282\u028d\3\2\2\2")
        buf.write("\u0283\u0284\5j\66\2\u0284\u0285\t\4\2\2\u0285\u0286\5")
        buf.write("l\67\6\u0286\u028d\3\2\2\2\u0287\u0288\7\63\2\2\u0288")
        buf.write("\u0289\5l\67\2\u0289\u028a\7\64\2\2\u028a\u028d\3\2\2")
        buf.write("\2\u028b\u028d\5~@\2\u028c\u027e\3\2\2\2\u028c\u0283\3")
        buf.write("\2\2\2\u028c\u0287\3\2\2\2\u028c\u028b\3\2\2\2\u028d\u029c")
        buf.write("\3\2\2\2\u028e\u028f\f\n\2\2\u028f\u0290\t\3\2\2\u0290")
        buf.write("\u029b\5l\67\13\u0291\u0292\f\7\2\2\u0292\u0293\t\4\2")
        buf.write("\2\u0293\u029b\5l\67\b\u0294\u0295\f\b\2\2\u0295\u0296")
        buf.write("\t\3\2\2\u0296\u029b\5j\66\2\u0297\u0298\f\5\2\2\u0298")
        buf.write("\u0299\t\4\2\2\u0299\u029b\5j\66\2\u029a\u028e\3\2\2\2")
        buf.write("\u029a\u0291\3\2\2\2\u029a\u0294\3\2\2\2\u029a\u0297\3")
        buf.write("\2\2\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d")
        buf.write("\3\2\2\2\u029dm\3\2\2\2\u029e\u029c\3\2\2\2\u029f\u02a0")
        buf.write("\b8\1\2\u02a0\u02a1\5j\66\2\u02a1\u02a2\7\31\2\2\u02a2")
        buf.write("\u02a3\5n8\5\u02a3\u02a6\3\2\2\2\u02a4\u02a6\5|?\2\u02a5")
        buf.write("\u029f\3\2\2\2\u02a5\u02a4\3\2\2\2\u02a6\u02af\3\2\2\2")
        buf.write("\u02a7\u02a8\f\4\2\2\u02a8\u02a9\7\27\2\2\u02a9\u02ae")
        buf.write("\5n8\5\u02aa\u02ab\f\6\2\2\u02ab\u02ac\7\31\2\2\u02ac")
        buf.write("\u02ae\5j\66\2\u02ad\u02a7\3\2\2\2\u02ad\u02aa\3\2\2\2")
        buf.write("\u02ae\u02b1\3\2\2\2\u02af\u02ad\3\2\2\2\u02af\u02b0\3")
        buf.write("\2\2\2\u02b0o\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02b3")
        buf.write("\5r:\2\u02b3\u02b4\7*\2\2\u02b4\u02b5\5p9\2\u02b5\u02c8")
        buf.write("\3\2\2\2\u02b6\u02b7\5r:\2\u02b7\u02b8\7\60\2\2\u02b8")
        buf.write("\u02b9\5p9\2\u02b9\u02c8\3\2\2\2\u02ba\u02bb\5r:\2\u02bb")
        buf.write("\u02bc\7+\2\2\u02bc\u02bd\5p9\2\u02bd\u02c8\3\2\2\2\u02be")
        buf.write("\u02bf\5r:\2\u02bf\u02c0\7\61\2\2\u02c0\u02c1\5p9\2\u02c1")
        buf.write("\u02c8\3\2\2\2\u02c2\u02c3\7\63\2\2\u02c3\u02c4\5p9\2")
        buf.write("\u02c4\u02c5\7\64\2\2\u02c5\u02c8\3\2\2\2\u02c6\u02c8")
        buf.write("\5r:\2\u02c7\u02b2\3\2\2\2\u02c7\u02b6\3\2\2\2\u02c7\u02ba")
        buf.write("\3\2\2\2\u02c7\u02be\3\2\2\2\u02c7\u02c2\3\2\2\2\u02c7")
        buf.write("\u02c6\3\2\2\2\u02c8q\3\2\2\2\u02c9\u02ca\5t;\2\u02ca")
        buf.write("\u02cb\t\5\2\2\u02cb\u02cc\5t;\2\u02cc\u02d2\3\2\2\2\u02cd")
        buf.write("\u02ce\5t;\2\u02ce\u02cf\t\6\2\2\u02cf\u02d0\5t;\2\u02d0")
        buf.write("\u02d2\3\2\2\2\u02d1\u02c9\3\2\2\2\u02d1\u02cd\3\2\2\2")
        buf.write("\u02d2s\3\2\2\2\u02d3\u02d7\5\64\33\2\u02d4\u02d7\5d\63")
        buf.write("\2\u02d5\u02d7\5\u0086D\2\u02d6\u02d3\3\2\2\2\u02d6\u02d4")
        buf.write("\3\2\2\2\u02d6\u02d5\3\2\2\2\u02d7u\3\2\2\2\u02d8\u02d9")
        buf.write("\5\u0086D\2\u02d9w\3\2\2\2\u02da\u02db\b=\1\2\u02db\u02f5")
        buf.write("\5v<\2\u02dc\u02f5\5\\/\2\u02dd\u02f5\5^\60\2\u02de\u02f5")
        buf.write("\5j\66\2\u02df\u02f5\5l\67\2\u02e0\u02f5\5n8\2\u02e1\u02f5")
        buf.write("\5\n\6\2\u02e2\u02f5\5\b\5\2\u02e3\u02f5\5T+\2\u02e4\u02f5")
        buf.write("\5Z.\2\u02e5\u02f5\5X-\2\u02e6\u02f5\5V,\2\u02e7\u02f5")
        buf.write("\5R*\2\u02e8\u02f5\5&\24\2\u02e9\u02f5\5|?\2\u02ea\u02f5")
        buf.write("\5\u0082B\2\u02eb\u02f5\5~@\2\u02ec\u02f5\5\u0080A\2\u02ed")
        buf.write("\u02f5\5\u0084C\2\u02ee\u02ef\t\7\2\2\u02ef\u02f5\5x=")
        buf.write("\f\u02f0\u02f1\7\63\2\2\u02f1\u02f2\5x=\2\u02f2\u02f3")
        buf.write("\7\64\2\2\u02f3\u02f5\3\2\2\2\u02f4\u02da\3\2\2\2\u02f4")
        buf.write("\u02dc\3\2\2\2\u02f4\u02dd\3\2\2\2\u02f4\u02de\3\2\2\2")
        buf.write("\u02f4\u02df\3\2\2\2\u02f4\u02e0\3\2\2\2\u02f4\u02e1\3")
        buf.write("\2\2\2\u02f4\u02e2\3\2\2\2\u02f4\u02e3\3\2\2\2\u02f4\u02e4")
        buf.write("\3\2\2\2\u02f4\u02e5\3\2\2\2\u02f4\u02e6\3\2\2\2\u02f4")
        buf.write("\u02e7\3\2\2\2\u02f4\u02e8\3\2\2\2\u02f4\u02e9\3\2\2\2")
        buf.write("\u02f4\u02ea\3\2\2\2\u02f4\u02eb\3\2\2\2\u02f4\u02ec\3")
        buf.write("\2\2\2\u02f4\u02ed\3\2\2\2\u02f4\u02ee\3\2\2\2\u02f4\u02f0")
        buf.write("\3\2\2\2\u02f5\u0313\3\2\2\2\u02f6\u02f7\f\r\2\2\u02f7")
        buf.write("\u02f8\7\34\2\2\u02f8\u0312\5x=\16\u02f9\u02fa\f\13\2")
        buf.write("\2\u02fa\u02fb\t\3\2\2\u02fb\u0312\5x=\f\u02fc\u02fd\f")
        buf.write("\n\2\2\u02fd\u02fe\t\4\2\2\u02fe\u0312\5x=\13\u02ff\u0300")
        buf.write("\f\t\2\2\u0300\u0301\t\b\2\2\u0301\u0312\5x=\n\u0302\u0303")
        buf.write("\f\b\2\2\u0303\u0304\7*\2\2\u0304\u0312\5x=\t\u0305\u0306")
        buf.write("\f\7\2\2\u0306\u0307\t\t\2\2\u0307\u0312\5x=\b\u0308\u0309")
        buf.write("\f\6\2\2\u0309\u030a\t\5\2\2\u030a\u0312\5x=\7\u030b\u030c")
        buf.write("\f\5\2\2\u030c\u030d\t\6\2\2\u030d\u0312\5x=\6\u030e\u030f")
        buf.write("\f\4\2\2\u030f\u0310\t\n\2\2\u0310\u0312\5x=\5\u0311\u02f6")
        buf.write("\3\2\2\2\u0311\u02f9\3\2\2\2\u0311\u02fc\3\2\2\2\u0311")
        buf.write("\u02ff\3\2\2\2\u0311\u0302\3\2\2\2\u0311\u0305\3\2\2\2")
        buf.write("\u0311\u0308\3\2\2\2\u0311\u030b\3\2\2\2\u0311\u030e\3")
        buf.write("\2\2\2\u0312\u0315\3\2\2\2\u0313\u0311\3\2\2\2\u0313\u0314")
        buf.write("\3\2\2\2\u0314y\3\2\2\2\u0315\u0313\3\2\2\2\u0316\u0317")
        buf.write("\7\22\2\2\u0317{\3\2\2\2\u0318\u0319\7\3\2\2\u0319}\3")
        buf.write("\2\2\2\u031a\u031b\7<\2\2\u031b\177\3\2\2\2\u031c\u031d")
        buf.write("\7;\2\2\u031d\u0081\3\2\2\2\u031e\u031f\t\13\2\2\u031f")
        buf.write("\u0083\3\2\2\2\u0320\u0321\7\67\2\2\u0321\u0085\3\2\2")
        buf.write("\2\u0322\u0323\7=\2\2\u0323\u0087\3\2\2\2\u0324\u0325")
        buf.write("\7>\2\2\u0325\u0089\3\2\2\2\u0326\u0327\7?\2\2\u0327\u008b")
        buf.write("\3\2\2\2\u0328\u0329\bG\1\2\u0329\u032c\7\5\2\2\u032a")
        buf.write("\u032c\5\u0090I\2\u032b\u0328\3\2\2\2\u032b\u032a\3\2")
        buf.write("\2\2\u032c\u0333\3\2\2\2\u032d\u032e\f\6\2\2\u032e\u0332")
        buf.write("\7\5\2\2\u032f\u0330\f\5\2\2\u0330\u0332\5\u0090I\2\u0331")
        buf.write("\u032d\3\2\2\2\u0331\u032f\3\2\2\2\u0332\u0335\3\2\2\2")
        buf.write("\u0333\u0331\3\2\2\2\u0333\u0334\3\2\2\2\u0334\u008d\3")
        buf.write("\2\2\2\u0335\u0333\3\2\2\2\u0336\u0337\7\r\2\2\u0337\u008f")
        buf.write("\3\2\2\2\u0338\u0339\7\6\2\2\u0339\u0091\3\2\2\2:\u0099")
        buf.write("\u00a1\u00ae\u00d5\u00d9\u00e2\u00ec\u0100\u010c\u0111")
        buf.write("\u0117\u011f\u0128\u013f\u0157\u016f\u018e\u0196\u01a0")
        buf.write("\u01af\u01bd\u01ca\u01cc\u01d7\u01e1\u01eb\u01f5\u01ff")
        buf.write("\u0211\u0217\u021b\u0222\u022a\u022e\u024a\u0261\u0263")
        buf.write("\u0269\u0271\u0279\u027b\u028c\u029a\u029c\u02a5\u02ad")
        buf.write("\u02af\u02c7\u02d1\u02d6\u02f4\u0311\u0313\u032b\u0331")
        buf.write("\u0333")
        return buf.getvalue()


class RubyParser ( Parser ):

    grammarFileName = "Ruby.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "','", "';'", "<INVALID>", 
                     "'require'", "'end'", "'def'", "'return'", "'pir'", 
                     "'if'", "'else'", "'elsif'", "'unless'", "'while'", 
                     "'retry'", "'break'", "'for'", "'do'", "'true'", "'false'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'**'", "'=='", 
                     "'!='", "'>'", "'<'", "'<='", "'>='", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'**='", "'&'", "'|'", 
                     "'^'", "'~'", "'<<'", "'>>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "'nil'" ]

    symbolicNames = [ "<INVALID>", "LITERAL", "COMMA", "SEMICOLON", "CRLF", 
                      "REQUIRE", "END", "DEF", "RETURN", "PIR", "IF", "ELSE", 
                      "ELSIF", "UNLESS", "WHILE", "RETRY", "BREAK", "FOR", 
                      "DO", "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "EXP", "EQUAL", "NOT_EQUAL", "GREATER", "LESS", 
                      "LESS_EQUAL", "GREATER_EQUAL", "ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "EXP_ASSIGN", "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT", 
                      "BIT_SHL", "BIT_SHR", "AND", "OR", "NOT", "LEFT_RBRACKET", 
                      "RIGHT_RBRACKET", "LEFT_SBRACKET", "RIGHT_SBRACKET", 
                      "NIL", "SL_COMMENT", "ML_COMMENT", "WS", "INT", "FLOAT", 
                      "ID", "ID_GLOBAL", "ID_FUNCTION" ]

    RULE_prog = 0
    RULE_expression_list = 1
    RULE_expression = 2
    RULE_global_get = 3
    RULE_global_set = 4
    RULE_global_result = 5
    RULE_function_inline_call = 6
    RULE_require_block = 7
    RULE_pir_inline = 8
    RULE_pir_expression_list = 9
    RULE_function_definition = 10
    RULE_function_definition_body = 11
    RULE_function_definition_header = 12
    RULE_function_name = 13
    RULE_function_definition_params = 14
    RULE_function_definition_params_list = 15
    RULE_function_definition_param_id = 16
    RULE_return_statement = 17
    RULE_function_call = 18
    RULE_function_call_param_list = 19
    RULE_function_call_params = 20
    RULE_function_param = 21
    RULE_function_unnamed_param = 22
    RULE_function_named_param = 23
    RULE_function_call_assignment = 24
    RULE_all_result = 25
    RULE_elsif_statement = 26
    RULE_if_elsif_statement = 27
    RULE_if_statement = 28
    RULE_unless_statement = 29
    RULE_while_statement = 30
    RULE_for_statement = 31
    RULE_init_expression = 32
    RULE_all_assignment = 33
    RULE_for_init_list = 34
    RULE_cond_expression = 35
    RULE_loop_expression = 36
    RULE_for_loop_list = 37
    RULE_statement_body = 38
    RULE_statement_expression_list = 39
    RULE_assignment = 40
    RULE_dynamic_assignment = 41
    RULE_int_assignment = 42
    RULE_float_assignment = 43
    RULE_string_assignment = 44
    RULE_initial_array_assignment = 45
    RULE_array_assignment = 46
    RULE_array_definition = 47
    RULE_array_definition_elements = 48
    RULE_array_selector = 49
    RULE_dynamic_result = 50
    RULE_dynamic = 51
    RULE_int_result = 52
    RULE_float_result = 53
    RULE_string_result = 54
    RULE_comparison_list = 55
    RULE_comparison = 56
    RULE_comp_var = 57
    RULE_lvalue = 58
    RULE_rvalue = 59
    RULE_break_expression = 60
    RULE_literal_t = 61
    RULE_float_t = 62
    RULE_int_t = 63
    RULE_bool_t = 64
    RULE_nil_t = 65
    RULE_idd = 66
    RULE_id_global = 67
    RULE_id_function = 68
    RULE_terminator = 69
    RULE_else_token = 70
    RULE_crlf = 71

    ruleNames =  [ "prog", "expression_list", "expression", "global_get", 
                   "global_set", "global_result", "function_inline_call", 
                   "require_block", "pir_inline", "pir_expression_list", 
                   "function_definition", "function_definition_body", "function_definition_header", 
                   "function_name", "function_definition_params", "function_definition_params_list", 
                   "function_definition_param_id", "return_statement", "function_call", 
                   "function_call_param_list", "function_call_params", "function_param", 
                   "function_unnamed_param", "function_named_param", "function_call_assignment", 
                   "all_result", "elsif_statement", "if_elsif_statement", 
                   "if_statement", "unless_statement", "while_statement", 
                   "for_statement", "init_expression", "all_assignment", 
                   "for_init_list", "cond_expression", "loop_expression", 
                   "for_loop_list", "statement_body", "statement_expression_list", 
                   "assignment", "dynamic_assignment", "int_assignment", 
                   "float_assignment", "string_assignment", "initial_array_assignment", 
                   "array_assignment", "array_definition", "array_definition_elements", 
                   "array_selector", "dynamic_result", "dynamic", "int_result", 
                   "float_result", "string_result", "comparison_list", "comparison", 
                   "comp_var", "lvalue", "rvalue", "break_expression", "literal_t", 
                   "float_t", "int_t", "bool_t", "nil_t", "idd", "id_global", 
                   "id_function", "terminator", "else_token", "crlf" ]

    EOF = Token.EOF
    LITERAL=1
    COMMA=2
    SEMICOLON=3
    CRLF=4
    REQUIRE=5
    END=6
    DEF=7
    RETURN=8
    PIR=9
    IF=10
    ELSE=11
    ELSIF=12
    UNLESS=13
    WHILE=14
    RETRY=15
    BREAK=16
    FOR=17
    DO=18
    TRUE=19
    FALSE=20
    PLUS=21
    MINUS=22
    MUL=23
    DIV=24
    MOD=25
    EXP=26
    EQUAL=27
    NOT_EQUAL=28
    GREATER=29
    LESS=30
    LESS_EQUAL=31
    GREATER_EQUAL=32
    ASSIGN=33
    PLUS_ASSIGN=34
    MINUS_ASSIGN=35
    MUL_ASSIGN=36
    DIV_ASSIGN=37
    MOD_ASSIGN=38
    EXP_ASSIGN=39
    BIT_AND=40
    BIT_OR=41
    BIT_XOR=42
    BIT_NOT=43
    BIT_SHL=44
    BIT_SHR=45
    AND=46
    OR=47
    NOT=48
    LEFT_RBRACKET=49
    RIGHT_RBRACKET=50
    LEFT_SBRACKET=51
    RIGHT_SBRACKET=52
    NIL=53
    SL_COMMENT=54
    ML_COMMENT=55
    WS=56
    INT=57
    FLOAT=58
    ID=59
    ID_GLOBAL=60
    ID_FUNCTION=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RubyParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expression_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RubyParser.ExpressionContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)



    def expression_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.LITERAL, RubyParser.REQUIRE, RubyParser.DEF, RubyParser.RETURN, RubyParser.PIR, RubyParser.IF, RubyParser.UNLESS, RubyParser.WHILE, RubyParser.FOR, RubyParser.TRUE, RubyParser.FALSE, RubyParser.BIT_NOT, RubyParser.NOT, RubyParser.LEFT_RBRACKET, RubyParser.NIL, RubyParser.INT, RubyParser.FLOAT, RubyParser.ID, RubyParser.ID_GLOBAL, RubyParser.ID_FUNCTION]:
                self.state = 147
                self.expression()
                self.state = 148
                self.terminator(0)
                pass
            elif token in [RubyParser.SEMICOLON, RubyParser.CRLF]:
                self.state = 150
                self.terminator(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Expression_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_list)
                    self.state = 153
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 154
                    self.expression()
                    self.state = 155
                    self.terminator(0) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition(self):
            return self.getTypedRuleContext(RubyParser.Function_definitionContext,0)


        def function_inline_call(self):
            return self.getTypedRuleContext(RubyParser.Function_inline_callContext,0)


        def require_block(self):
            return self.getTypedRuleContext(RubyParser.Require_blockContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(RubyParser.If_statementContext,0)


        def unless_statement(self):
            return self.getTypedRuleContext(RubyParser.Unless_statementContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(RubyParser.RvalueContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(RubyParser.Return_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(RubyParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(RubyParser.For_statementContext,0)


        def pir_inline(self):
            return self.getTypedRuleContext(RubyParser.Pir_inlineContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = RubyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.function_inline_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.require_block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.unless_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.rvalue(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.while_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 170
                self.for_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 171
                self.pir_inline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_getContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_name = None # LvalueContext
            self.op = None # Token
            self.global_name = None # Id_globalContext

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_get

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_get" ):
                listener.enterGlobal_get(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_get" ):
                listener.exitGlobal_get(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_get" ):
                return visitor.visitGlobal_get(self)
            else:
                return visitor.visitChildren(self)




    def global_get(self):

        localctx = RubyParser.Global_getContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_global_get)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            localctx.var_name = self.lvalue()
            self.state = 175
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 176
            localctx.global_name = self.id_global()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_setContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.global_name = None # Id_globalContext
            self.op = None # Token
            self.result = None # All_resultContext

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_set" ):
                listener.enterGlobal_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_set" ):
                listener.exitGlobal_set(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_set" ):
                return visitor.visitGlobal_set(self)
            else:
                return visitor.visitChildren(self)




    def global_set(self):

        localctx = RubyParser.Global_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_global_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            localctx.global_name = self.id_global()
            self.state = 179
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 180
            localctx.result = self.all_result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_global_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_result" ):
                listener.enterGlobal_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_result" ):
                listener.exitGlobal_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_result" ):
                return visitor.visitGlobal_result(self)
            else:
                return visitor.visitChildren(self)




    def global_result(self):

        localctx = RubyParser.Global_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_global_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.id_global()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_inline_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(RubyParser.Function_callContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_inline_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_inline_call" ):
                listener.enterFunction_inline_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_inline_call" ):
                listener.exitFunction_inline_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_inline_call" ):
                return visitor.visitFunction_inline_call(self)
            else:
                return visitor.visitChildren(self)




    def function_inline_call(self):

        localctx = RubyParser.Function_inline_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_inline_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Require_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIRE(self):
            return self.getToken(RubyParser.REQUIRE, 0)

        def literal_t(self):
            return self.getTypedRuleContext(RubyParser.Literal_tContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_require_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequire_block" ):
                listener.enterRequire_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequire_block" ):
                listener.exitRequire_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequire_block" ):
                return visitor.visitRequire_block(self)
            else:
                return visitor.visitChildren(self)




    def require_block(self):

        localctx = RubyParser.Require_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_require_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(RubyParser.REQUIRE)
            self.state = 187
            self.literal_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pir_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIR(self):
            return self.getToken(RubyParser.PIR, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def pir_expression_list(self):
            return self.getTypedRuleContext(RubyParser.Pir_expression_listContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_pir_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPir_inline" ):
                listener.enterPir_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPir_inline" ):
                listener.exitPir_inline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPir_inline" ):
                return visitor.visitPir_inline(self)
            else:
                return visitor.visitChildren(self)




    def pir_inline(self):

        localctx = RubyParser.Pir_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pir_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(RubyParser.PIR)
            self.state = 190
            self.crlf()
            self.state = 191
            self.pir_expression_list()
            self.state = 192
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pir_expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_pir_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPir_expression_list" ):
                listener.enterPir_expression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPir_expression_list" ):
                listener.exitPir_expression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPir_expression_list" ):
                return visitor.visitPir_expression_list(self)
            else:
                return visitor.visitChildren(self)




    def pir_expression_list(self):

        localctx = RubyParser.Pir_expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pir_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expression_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition_header(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_headerContext,0)


        def function_definition_body(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = RubyParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.function_definition_header()
            self.state = 197
            self.function_definition_body()
            self.state = 198
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definition_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(RubyParser.Expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_definition_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_body" ):
                listener.enterFunction_definition_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_body" ):
                listener.exitFunction_definition_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_body" ):
                return visitor.visitFunction_definition_body(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_body(self):

        localctx = RubyParser.Function_definition_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_definition_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expression_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definition_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(RubyParser.DEF, 0)

        def function_name(self):
            return self.getTypedRuleContext(RubyParser.Function_nameContext,0)


        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def function_definition_params(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_paramsContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_definition_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_header" ):
                listener.enterFunction_definition_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_header" ):
                listener.exitFunction_definition_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_header" ):
                return visitor.visitFunction_definition_header(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_header(self):

        localctx = RubyParser.Function_definition_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_function_definition_header)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(RubyParser.DEF)
                self.state = 203
                self.function_name()
                self.state = 204
                self.crlf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(RubyParser.DEF)
                self.state = 207
                self.function_name()
                self.state = 208
                self.function_definition_params()
                self.state = 209
                self.crlf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_function(self):
            return self.getTypedRuleContext(RubyParser.Id_functionContext,0)


        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_name" ):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = RubyParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_name)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID_FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.id_function()
                pass
            elif token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.idd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definition_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def function_definition_params_list(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_params_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_definition_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_params" ):
                listener.enterFunction_definition_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_params" ):
                listener.exitFunction_definition_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_params" ):
                return visitor.visitFunction_definition_params(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_params(self):

        localctx = RubyParser.Function_definition_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_definition_params)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 218
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 220
                self.function_definition_params_list(0)
                self.state = 221
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.function_definition_params_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definition_params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition_param_id(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_param_idContext,0)


        def function_definition_params_list(self):
            return self.getTypedRuleContext(RubyParser.Function_definition_params_listContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_function_definition_params_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_params_list" ):
                listener.enterFunction_definition_params_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_params_list" ):
                listener.exitFunction_definition_params_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_params_list" ):
                return visitor.visitFunction_definition_params_list(self)
            else:
                return visitor.visitChildren(self)



    def function_definition_params_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Function_definition_params_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_function_definition_params_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.function_definition_param_id()
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Function_definition_params_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_function_definition_params_list)
                    self.state = 229
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 230
                    self.match(RubyParser.COMMA)
                    self.state = 231
                    self.function_definition_param_id() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_definition_param_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_definition_param_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition_param_id" ):
                listener.enterFunction_definition_param_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition_param_id" ):
                listener.exitFunction_definition_param_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition_param_id" ):
                return visitor.visitFunction_definition_param_id(self)
            else:
                return visitor.visitChildren(self)




    def function_definition_param_id(self):

        localctx = RubyParser.Function_definition_param_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_definition_param_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.idd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(RubyParser.RETURN, 0)

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = RubyParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(RubyParser.RETURN)
            self.state = 240
            self.all_result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Function_nameContext
            self.params = None # Function_call_param_listContext

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def function_name(self):
            return self.getTypedRuleContext(RubyParser.Function_nameContext,0)


        def function_call_param_list(self):
            return self.getTypedRuleContext(RubyParser.Function_call_param_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = RubyParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_call)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                localctx.name = self.function_name()
                self.state = 243
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 244
                localctx.params = self.function_call_param_list()
                self.state = 245
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                localctx.name = self.function_name()
                self.state = 248
                localctx.params = self.function_call_param_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                localctx.name = self.function_name()
                self.state = 251
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 252
                self.match(RubyParser.RIGHT_RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call_params(self):
            return self.getTypedRuleContext(RubyParser.Function_call_paramsContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_call_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_param_list" ):
                listener.enterFunction_call_param_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_param_list" ):
                listener.exitFunction_call_param_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_param_list" ):
                return visitor.visitFunction_call_param_list(self)
            else:
                return visitor.visitChildren(self)




    def function_call_param_list(self):

        localctx = RubyParser.Function_call_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_call_param_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.function_call_params(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_param(self):
            return self.getTypedRuleContext(RubyParser.Function_paramContext,0)


        def function_call_params(self):
            return self.getTypedRuleContext(RubyParser.Function_call_paramsContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_function_call_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_params" ):
                listener.enterFunction_call_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_params" ):
                listener.exitFunction_call_params(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_params" ):
                return visitor.visitFunction_call_params(self)
            else:
                return visitor.visitChildren(self)



    def function_call_params(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Function_call_paramsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_function_call_params, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.function_param()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Function_call_paramsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_function_call_params)
                    self.state = 261
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 262
                    self.match(RubyParser.COMMA)
                    self.state = 263
                    self.function_param() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_unnamed_param(self):
            return self.getTypedRuleContext(RubyParser.Function_unnamed_paramContext,0)


        def function_named_param(self):
            return self.getTypedRuleContext(RubyParser.Function_named_paramContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_param" ):
                listener.enterFunction_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_param" ):
                listener.exitFunction_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_param" ):
                return visitor.visitFunction_param(self)
            else:
                return visitor.visitChildren(self)




    def function_param(self):

        localctx = RubyParser.Function_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 269
                self.function_unnamed_param()
                pass

            elif la_ == 2:
                self.state = 270
                self.function_named_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_unnamed_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_unnamed_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_unnamed_param" ):
                listener.enterFunction_unnamed_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_unnamed_param" ):
                listener.exitFunction_unnamed_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_unnamed_param" ):
                return visitor.visitFunction_unnamed_param(self)
            else:
                return visitor.visitChildren(self)




    def function_unnamed_param(self):

        localctx = RubyParser.Function_unnamed_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_unnamed_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 273
                self.int_result(0)
                pass

            elif la_ == 2:
                self.state = 274
                self.float_result(0)
                pass

            elif la_ == 3:
                self.state = 275
                self.string_result(0)
                pass

            elif la_ == 4:
                self.state = 276
                self.dynamic_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_named_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_named_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_named_param" ):
                listener.enterFunction_named_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_named_param" ):
                listener.exitFunction_named_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_named_param" ):
                return visitor.visitFunction_named_param(self)
            else:
                return visitor.visitChildren(self)




    def function_named_param(self):

        localctx = RubyParser.Function_named_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_function_named_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.idd()
            self.state = 280
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 281
                self.int_result(0)
                pass

            elif la_ == 2:
                self.state = 282
                self.float_result(0)
                pass

            elif la_ == 3:
                self.state = 283
                self.string_result(0)
                pass

            elif la_ == 4:
                self.state = 284
                self.dynamic_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(RubyParser.Function_callContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_function_call_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_assignment" ):
                listener.enterFunction_call_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_assignment" ):
                listener.exitFunction_call_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_assignment" ):
                return visitor.visitFunction_call_assignment(self)
            else:
                return visitor.visitChildren(self)




    def function_call_assignment(self):

        localctx = RubyParser.Function_call_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def global_result(self):
            return self.getTypedRuleContext(RubyParser.Global_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_all_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_result" ):
                listener.enterAll_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_result" ):
                listener.exitAll_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_result" ):
                return visitor.visitAll_result(self)
            else:
                return visitor.visitChildren(self)




    def all_result(self):

        localctx = RubyParser.All_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_all_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 289
                self.int_result(0)
                pass

            elif la_ == 2:
                self.state = 290
                self.float_result(0)
                pass

            elif la_ == 3:
                self.state = 291
                self.string_result(0)
                pass

            elif la_ == 4:
                self.state = 292
                self.dynamic_result(0)
                pass

            elif la_ == 5:
                self.state = 293
                self.global_result()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elsif_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_elsif_statement(self):
            return self.getTypedRuleContext(RubyParser.If_elsif_statementContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_elsif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsif_statement" ):
                listener.enterElsif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsif_statement" ):
                listener.exitElsif_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsif_statement" ):
                return visitor.visitElsif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elsif_statement(self):

        localctx = RubyParser.Elsif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elsif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.if_elsif_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_elsif_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSIF(self):
            return self.getToken(RubyParser.ELSIF, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def statement_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Statement_bodyContext)
            else:
                return self.getTypedRuleContext(RubyParser.Statement_bodyContext,i)


        def else_token(self):
            return self.getTypedRuleContext(RubyParser.Else_tokenContext,0)


        def if_elsif_statement(self):
            return self.getTypedRuleContext(RubyParser.If_elsif_statementContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_if_elsif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_elsif_statement" ):
                listener.enterIf_elsif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_elsif_statement" ):
                listener.exitIf_elsif_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_elsif_statement" ):
                return visitor.visitIf_elsif_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_elsif_statement(self):

        localctx = RubyParser.If_elsif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_elsif_statement)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(RubyParser.ELSIF)
                self.state = 299
                self.cond_expression()
                self.state = 300
                self.crlf()
                self.state = 301
                self.statement_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(RubyParser.ELSIF)
                self.state = 304
                self.cond_expression()
                self.state = 305
                self.crlf()
                self.state = 306
                self.statement_body()
                self.state = 307
                self.else_token()
                self.state = 308
                self.crlf()
                self.state = 309
                self.statement_body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(RubyParser.ELSIF)
                self.state = 312
                self.cond_expression()
                self.state = 313
                self.crlf()
                self.state = 314
                self.statement_body()
                self.state = 315
                self.if_elsif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RubyParser.IF, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def statement_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Statement_bodyContext)
            else:
                return self.getTypedRuleContext(RubyParser.Statement_bodyContext,i)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def else_token(self):
            return self.getTypedRuleContext(RubyParser.Else_tokenContext,0)


        def elsif_statement(self):
            return self.getTypedRuleContext(RubyParser.Elsif_statementContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = RubyParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(RubyParser.IF)
                self.state = 320
                self.cond_expression()
                self.state = 321
                self.crlf()
                self.state = 322
                self.statement_body()
                self.state = 323
                self.match(RubyParser.END)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(RubyParser.IF)
                self.state = 326
                self.cond_expression()
                self.state = 327
                self.crlf()
                self.state = 328
                self.statement_body()
                self.state = 329
                self.else_token()
                self.state = 330
                self.crlf()
                self.state = 331
                self.statement_body()
                self.state = 332
                self.match(RubyParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.match(RubyParser.IF)
                self.state = 335
                self.cond_expression()
                self.state = 336
                self.crlf()
                self.state = 337
                self.statement_body()
                self.state = 338
                self.elsif_statement()
                self.state = 339
                self.match(RubyParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unless_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNLESS(self):
            return self.getToken(RubyParser.UNLESS, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def crlf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.CrlfContext)
            else:
                return self.getTypedRuleContext(RubyParser.CrlfContext,i)


        def statement_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Statement_bodyContext)
            else:
                return self.getTypedRuleContext(RubyParser.Statement_bodyContext,i)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def else_token(self):
            return self.getTypedRuleContext(RubyParser.Else_tokenContext,0)


        def elsif_statement(self):
            return self.getTypedRuleContext(RubyParser.Elsif_statementContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_unless_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnless_statement" ):
                listener.enterUnless_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnless_statement" ):
                listener.exitUnless_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnless_statement" ):
                return visitor.visitUnless_statement(self)
            else:
                return visitor.visitChildren(self)




    def unless_statement(self):

        localctx = RubyParser.Unless_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unless_statement)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(RubyParser.UNLESS)
                self.state = 344
                self.cond_expression()
                self.state = 345
                self.crlf()
                self.state = 346
                self.statement_body()
                self.state = 347
                self.match(RubyParser.END)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(RubyParser.UNLESS)
                self.state = 350
                self.cond_expression()
                self.state = 351
                self.crlf()
                self.state = 352
                self.statement_body()
                self.state = 353
                self.else_token()
                self.state = 354
                self.crlf()
                self.state = 355
                self.statement_body()
                self.state = 356
                self.match(RubyParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.match(RubyParser.UNLESS)
                self.state = 359
                self.cond_expression()
                self.state = 360
                self.crlf()
                self.state = 361
                self.statement_body()
                self.state = 362
                self.elsif_statement()
                self.state = 363
                self.match(RubyParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(RubyParser.WHILE, 0)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def DO(self):
            return self.getToken(RubyParser.DO, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = RubyParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(RubyParser.WHILE)
            self.state = 368
            self.cond_expression()
            self.state = 369
            self.match(RubyParser.DO)
            self.state = 370
            self.crlf()
            self.state = 371
            self.statement_body()
            self.state = 372
            self.match(RubyParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RubyParser.FOR, 0)

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def init_expression(self):
            return self.getTypedRuleContext(RubyParser.Init_expressionContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(RubyParser.SEMICOLON)
            else:
                return self.getToken(RubyParser.SEMICOLON, i)

        def cond_expression(self):
            return self.getTypedRuleContext(RubyParser.Cond_expressionContext,0)


        def loop_expression(self):
            return self.getTypedRuleContext(RubyParser.Loop_expressionContext,0)


        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def statement_body(self):
            return self.getTypedRuleContext(RubyParser.Statement_bodyContext,0)


        def END(self):
            return self.getToken(RubyParser.END, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = RubyParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_statement)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(RubyParser.FOR)
                self.state = 375
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 376
                self.init_expression()
                self.state = 377
                self.match(RubyParser.SEMICOLON)
                self.state = 378
                self.cond_expression()
                self.state = 379
                self.match(RubyParser.SEMICOLON)
                self.state = 380
                self.loop_expression()
                self.state = 381
                self.match(RubyParser.RIGHT_RBRACKET)
                self.state = 382
                self.crlf()
                self.state = 383
                self.statement_body()
                self.state = 384
                self.match(RubyParser.END)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.match(RubyParser.FOR)
                self.state = 387
                self.init_expression()
                self.state = 388
                self.match(RubyParser.SEMICOLON)
                self.state = 389
                self.cond_expression()
                self.state = 390
                self.match(RubyParser.SEMICOLON)
                self.state = 391
                self.loop_expression()
                self.state = 392
                self.crlf()
                self.state = 393
                self.statement_body()
                self.state = 394
                self.match(RubyParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_init_list(self):
            return self.getTypedRuleContext(RubyParser.For_init_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_init_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit_expression" ):
                listener.enterInit_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit_expression" ):
                listener.exitInit_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_expression" ):
                return visitor.visitInit_expression(self)
            else:
                return visitor.visitChildren(self)




    def init_expression(self):

        localctx = RubyParser.Init_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_init_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.for_init_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_assignment(self):
            return self.getTypedRuleContext(RubyParser.Int_assignmentContext,0)


        def float_assignment(self):
            return self.getTypedRuleContext(RubyParser.Float_assignmentContext,0)


        def string_assignment(self):
            return self.getTypedRuleContext(RubyParser.String_assignmentContext,0)


        def dynamic_assignment(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_assignmentContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_all_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_assignment" ):
                listener.enterAll_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_assignment" ):
                listener.exitAll_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_assignment" ):
                return visitor.visitAll_assignment(self)
            else:
                return visitor.visitChildren(self)




    def all_assignment(self):

        localctx = RubyParser.All_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_all_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 400
                self.int_assignment()
                pass

            elif la_ == 2:
                self.state = 401
                self.float_assignment()
                pass

            elif la_ == 3:
                self.state = 402
                self.string_assignment()
                pass

            elif la_ == 4:
                self.state = 403
                self.dynamic_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_init_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_assignment(self):
            return self.getTypedRuleContext(RubyParser.All_assignmentContext,0)


        def for_init_list(self):
            return self.getTypedRuleContext(RubyParser.For_init_listContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_for_init_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_init_list" ):
                listener.enterFor_init_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_init_list" ):
                listener.exitFor_init_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init_list" ):
                return visitor.visitFor_init_list(self)
            else:
                return visitor.visitChildren(self)



    def for_init_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.For_init_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_for_init_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.all_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.For_init_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_for_init_list)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    self.match(RubyParser.COMMA)
                    self.state = 411
                    self.all_assignment() 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Cond_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_list(self):
            return self.getTypedRuleContext(RubyParser.Comparison_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_cond_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_expression" ):
                listener.enterCond_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_expression" ):
                listener.exitCond_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_expression" ):
                return visitor.visitCond_expression(self)
            else:
                return visitor.visitChildren(self)




    def cond_expression(self):

        localctx = RubyParser.Cond_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_cond_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.comparison_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop_list(self):
            return self.getTypedRuleContext(RubyParser.For_loop_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_loop_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_expression" ):
                listener.enterLoop_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_expression" ):
                listener.exitLoop_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_expression" ):
                return visitor.visitLoop_expression(self)
            else:
                return visitor.visitChildren(self)




    def loop_expression(self):

        localctx = RubyParser.Loop_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_loop_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.for_loop_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_assignment(self):
            return self.getTypedRuleContext(RubyParser.All_assignmentContext,0)


        def for_loop_list(self):
            return self.getTypedRuleContext(RubyParser.For_loop_listContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_for_loop_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_list" ):
                listener.enterFor_loop_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_list" ):
                listener.exitFor_loop_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_list" ):
                return visitor.visitFor_loop_list(self)
            else:
                return visitor.visitChildren(self)



    def for_loop_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.For_loop_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_for_loop_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.all_assignment()
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.For_loop_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_for_loop_list)
                    self.state = 424
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 425
                    self.match(RubyParser.COMMA)
                    self.state = 426
                    self.all_assignment() 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Statement_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_expression_list(self):
            return self.getTypedRuleContext(RubyParser.Statement_expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statement_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_body" ):
                listener.enterStatement_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_body" ):
                listener.exitStatement_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_body" ):
                return visitor.visitStatement_body(self)
            else:
                return visitor.visitChildren(self)




    def statement_body(self):

        localctx = RubyParser.Statement_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.statement_expression_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RubyParser.ExpressionContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def RETRY(self):
            return self.getToken(RubyParser.RETRY, 0)

        def break_expression(self):
            return self.getTypedRuleContext(RubyParser.Break_expressionContext,0)


        def statement_expression_list(self):
            return self.getTypedRuleContext(RubyParser.Statement_expression_listContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_statement_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_expression_list" ):
                listener.enterStatement_expression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_expression_list" ):
                listener.exitStatement_expression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_expression_list" ):
                return visitor.visitStatement_expression_list(self)
            else:
                return visitor.visitChildren(self)



    def statement_expression_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Statement_expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_statement_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.LITERAL, RubyParser.REQUIRE, RubyParser.DEF, RubyParser.RETURN, RubyParser.PIR, RubyParser.IF, RubyParser.UNLESS, RubyParser.WHILE, RubyParser.FOR, RubyParser.TRUE, RubyParser.FALSE, RubyParser.BIT_NOT, RubyParser.NOT, RubyParser.LEFT_RBRACKET, RubyParser.NIL, RubyParser.INT, RubyParser.FLOAT, RubyParser.ID, RubyParser.ID_GLOBAL, RubyParser.ID_FUNCTION]:
                self.state = 435
                self.expression()
                self.state = 436
                self.terminator(0)
                pass
            elif token in [RubyParser.RETRY]:
                self.state = 438
                self.match(RubyParser.RETRY)
                self.state = 439
                self.terminator(0)
                pass
            elif token in [RubyParser.BREAK]:
                self.state = 440
                self.break_expression()
                self.state = 441
                self.terminator(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 456
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Statement_expression_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_expression_list)
                        self.state = 445
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 446
                        self.expression()
                        self.state = 447
                        self.terminator(0)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Statement_expression_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_expression_list)
                        self.state = 449
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 450
                        self.match(RubyParser.RETRY)
                        self.state = 451
                        self.terminator(0)
                        pass

                    elif la_ == 3:
                        localctx = RubyParser.Statement_expression_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_expression_list)
                        self.state = 452
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 453
                        self.break_expression()
                        self.state = 454
                        self.terminator(0)
                        pass

             
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def rvalue(self):
            return self.getTypedRuleContext(RubyParser.RvalueContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = RubyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                localctx.var_id = self.lvalue()
                self.state = 462
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 463
                self.rvalue(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                localctx.var_id = self.lvalue()
                self.state = 466
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 467
                self.rvalue(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_dynamic_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_assignment" ):
                listener.enterDynamic_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_assignment" ):
                listener.exitDynamic_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_assignment" ):
                return visitor.visitDynamic_assignment(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_assignment(self):

        localctx = RubyParser.Dynamic_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dynamic_assignment)
        self._la = 0 # Token type
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                localctx.var_id = self.lvalue()
                self.state = 472
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 473
                self.dynamic_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                localctx.var_id = self.lvalue()
                self.state = 476
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 477
                self.dynamic_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_int_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_assignment" ):
                listener.enterInt_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_assignment" ):
                listener.exitInt_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_assignment" ):
                return visitor.visitInt_assignment(self)
            else:
                return visitor.visitChildren(self)




    def int_assignment(self):

        localctx = RubyParser.Int_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_int_assignment)
        self._la = 0 # Token type
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                localctx.var_id = self.lvalue()
                self.state = 482
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 483
                self.int_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                localctx.var_id = self.lvalue()
                self.state = 486
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 487
                self.int_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(RubyParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(RubyParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(RubyParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(RubyParser.MOD_ASSIGN, 0)

        def EXP_ASSIGN(self):
            return self.getToken(RubyParser.EXP_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_float_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_assignment" ):
                listener.enterFloat_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_assignment" ):
                listener.exitFloat_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_assignment" ):
                return visitor.visitFloat_assignment(self)
            else:
                return visitor.visitChildren(self)




    def float_assignment(self):

        localctx = RubyParser.Float_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_float_assignment)
        self._la = 0 # Token type
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                localctx.var_id = self.lvalue()
                self.state = 492
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 493
                self.float_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                localctx.var_id = self.lvalue()
                self.state = 496
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.PLUS_ASSIGN) | (1 << RubyParser.MINUS_ASSIGN) | (1 << RubyParser.MUL_ASSIGN) | (1 << RubyParser.DIV_ASSIGN) | (1 << RubyParser.MOD_ASSIGN) | (1 << RubyParser.EXP_ASSIGN))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 497
                self.float_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(RubyParser.PLUS_ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_string_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_assignment" ):
                listener.enterString_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_assignment" ):
                listener.exitString_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_assignment" ):
                return visitor.visitString_assignment(self)
            else:
                return visitor.visitChildren(self)




    def string_assignment(self):

        localctx = RubyParser.String_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_string_assignment)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                localctx.var_id = self.lvalue()
                self.state = 502
                localctx.op = self.match(RubyParser.ASSIGN)
                self.state = 503
                self.string_result(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                localctx.var_id = self.lvalue()
                self.state = 506
                localctx.op = self.match(RubyParser.PLUS_ASSIGN)
                self.state = 507
                self.string_result(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initial_array_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_id = None # LvalueContext
            self.op = None # Token

        def LEFT_SBRACKET(self):
            return self.getToken(RubyParser.LEFT_SBRACKET, 0)

        def RIGHT_SBRACKET(self):
            return self.getToken(RubyParser.RIGHT_SBRACKET, 0)

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_initial_array_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitial_array_assignment" ):
                listener.enterInitial_array_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitial_array_assignment" ):
                listener.exitInitial_array_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitial_array_assignment" ):
                return visitor.visitInitial_array_assignment(self)
            else:
                return visitor.visitChildren(self)




    def initial_array_assignment(self):

        localctx = RubyParser.Initial_array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_initial_array_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            localctx.var_id = self.lvalue()
            self.state = 512
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 513
            self.match(RubyParser.LEFT_SBRACKET)
            self.state = 514
            self.match(RubyParser.RIGHT_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.arr_def = None # Array_selectorContext
            self.op = None # Token
            self.arr_val = None # All_resultContext

        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def ASSIGN(self):
            return self.getToken(RubyParser.ASSIGN, 0)

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_array_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_assignment" ):
                listener.enterArray_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_assignment" ):
                listener.exitArray_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_assignment" ):
                return visitor.visitArray_assignment(self)
            else:
                return visitor.visitChildren(self)




    def array_assignment(self):

        localctx = RubyParser.Array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            localctx.arr_def = self.array_selector()
            self.state = 517
            localctx.op = self.match(RubyParser.ASSIGN)
            self.state = 518
            localctx.arr_val = self.all_result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_SBRACKET(self):
            return self.getToken(RubyParser.LEFT_SBRACKET, 0)

        def array_definition_elements(self):
            return self.getTypedRuleContext(RubyParser.Array_definition_elementsContext,0)


        def RIGHT_SBRACKET(self):
            return self.getToken(RubyParser.RIGHT_SBRACKET, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_array_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_definition" ):
                listener.enterArray_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_definition" ):
                listener.exitArray_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_definition" ):
                return visitor.visitArray_definition(self)
            else:
                return visitor.visitChildren(self)




    def array_definition(self):

        localctx = RubyParser.Array_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(RubyParser.LEFT_SBRACKET)
            self.state = 521
            self.array_definition_elements(0)
            self.state = 522
            self.match(RubyParser.RIGHT_SBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_definition_elementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def array_definition_elements(self):
            return self.getTypedRuleContext(RubyParser.Array_definition_elementsContext,0)


        def COMMA(self):
            return self.getToken(RubyParser.COMMA, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_array_definition_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_definition_elements" ):
                listener.enterArray_definition_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_definition_elements" ):
                listener.exitArray_definition_elements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_definition_elements" ):
                return visitor.visitArray_definition_elements(self)
            else:
                return visitor.visitChildren(self)



    def array_definition_elements(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Array_definition_elementsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_array_definition_elements, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 525
                self.int_result(0)
                pass

            elif la_ == 2:
                self.state = 526
                self.dynamic_result(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 537
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RubyParser.Array_definition_elementsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_definition_elements)
                    self.state = 529
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 530
                    self.match(RubyParser.COMMA)
                    self.state = 533
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        self.state = 531
                        self.int_result(0)
                        pass

                    elif la_ == 2:
                        self.state = 532
                        self.dynamic_result(0)
                        pass

             
                self.state = 539
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_selectorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def LEFT_SBRACKET(self):
            return self.getToken(RubyParser.LEFT_SBRACKET, 0)

        def RIGHT_SBRACKET(self):
            return self.getToken(RubyParser.RIGHT_SBRACKET, 0)

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def dynamic_result(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,0)


        def id_global(self):
            return self.getTypedRuleContext(RubyParser.Id_globalContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_array_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_selector" ):
                listener.enterArray_selector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_selector" ):
                listener.exitArray_selector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_selector" ):
                return visitor.visitArray_selector(self)
            else:
                return visitor.visitChildren(self)




    def array_selector(self):

        localctx = RubyParser.Array_selectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_selector)
        try:
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.idd()
                self.state = 541
                self.match(RubyParser.LEFT_SBRACKET)
                self.state = 544
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 542
                    self.int_result(0)
                    pass

                elif la_ == 2:
                    self.state = 543
                    self.dynamic_result(0)
                    pass


                self.state = 546
                self.match(RubyParser.RIGHT_SBRACKET)
                pass
            elif token in [RubyParser.ID_GLOBAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.id_global()
                self.state = 549
                self.match(RubyParser.LEFT_SBRACKET)
                self.state = 552
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 550
                    self.int_result(0)
                    pass

                elif la_ == 2:
                    self.state = 551
                    self.dynamic_result(0)
                    pass


                self.state = 554
                self.match(RubyParser.RIGHT_SBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def dynamic_result(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Dynamic_resultContext)
            else:
                return self.getTypedRuleContext(RubyParser.Dynamic_resultContext,i)


        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def dynamic(self):
            return self.getTypedRuleContext(RubyParser.DynamicContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_dynamic_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_result" ):
                listener.enterDynamic_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_result" ):
                listener.exitDynamic_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_result" ):
                return visitor.visitDynamic_result(self)
            else:
                return visitor.visitChildren(self)



    def dynamic_result(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Dynamic_resultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_dynamic_result, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 559
                self.int_result(0)
                self.state = 560
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 561
                self.dynamic_result(13)
                pass

            elif la_ == 2:
                self.state = 563
                self.float_result(0)
                self.state = 564
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 565
                self.dynamic_result(11)
                pass

            elif la_ == 3:
                self.state = 567
                self.string_result(0)
                self.state = 568
                localctx.op = self.match(RubyParser.MUL)
                self.state = 569
                self.dynamic_result(8)
                pass

            elif la_ == 4:
                self.state = 571
                self.int_result(0)
                self.state = 572
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 573
                self.dynamic_result(6)
                pass

            elif la_ == 5:
                self.state = 575
                self.float_result(0)
                self.state = 576
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 577
                self.dynamic_result(4)
                pass

            elif la_ == 6:
                self.state = 579
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 580
                self.dynamic_result(0)
                self.state = 581
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 7:
                self.state = 583
                self.dynamic()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 607
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 586
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 587
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 588
                        self.dynamic_result(11)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 589
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 590
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 591
                        self.dynamic_result(4)
                        pass

                    elif la_ == 3:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 592
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 593
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 594
                        self.int_result(0)
                        pass

                    elif la_ == 4:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 595
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 596
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 597
                        self.float_result(0)
                        pass

                    elif la_ == 5:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 598
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 599
                        localctx.op = self.match(RubyParser.MUL)
                        self.state = 600
                        self.string_result(0)
                        pass

                    elif la_ == 6:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 601
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 602
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 603
                        self.int_result(0)
                        pass

                    elif la_ == 7:
                        localctx = RubyParser.Dynamic_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_dynamic_result)
                        self.state = 604
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 605
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 606
                        self.float_result(0)
                        pass

             
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DynamicContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def function_call_assignment(self):
            return self.getTypedRuleContext(RubyParser.Function_call_assignmentContext,0)


        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_dynamic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic" ):
                listener.enterDynamic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic" ):
                listener.exitDynamic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic" ):
                return visitor.visitDynamic(self)
            else:
                return visitor.visitChildren(self)




    def dynamic(self):

        localctx = RubyParser.DynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_dynamic)
        try:
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.idd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                self.function_call_assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 614
                self.array_selector()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def int_result(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Int_resultContext)
            else:
                return self.getTypedRuleContext(RubyParser.Int_resultContext,i)


        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def int_t(self):
            return self.getTypedRuleContext(RubyParser.Int_tContext,0)


        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_int_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_result" ):
                listener.enterInt_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_result" ):
                listener.exitInt_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_result" ):
                return visitor.visitInt_result(self)
            else:
                return visitor.visitChildren(self)



    def int_result(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Int_resultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_int_result, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.LEFT_RBRACKET]:
                self.state = 618
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 619
                self.int_result(0)
                self.state = 620
                self.match(RubyParser.RIGHT_RBRACKET)
                pass
            elif token in [RubyParser.INT]:
                self.state = 622
                self.int_t()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 631
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Int_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_int_result)
                        self.state = 625
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 626
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 627
                        self.int_result(5)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Int_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_int_result)
                        self.state = 628
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 629
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 630
                        self.int_result(4)
                        pass

             
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Float_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def float_result(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Float_resultContext)
            else:
                return self.getTypedRuleContext(RubyParser.Float_resultContext,i)


        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def float_t(self):
            return self.getTypedRuleContext(RubyParser.Float_tContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_float_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_result" ):
                listener.enterFloat_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_result" ):
                listener.exitFloat_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_result" ):
                return visitor.visitFloat_result(self)
            else:
                return visitor.visitChildren(self)



    def float_result(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.Float_resultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_float_result, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 637
                self.int_result(0)
                self.state = 638
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 639
                self.float_result(7)
                pass

            elif la_ == 2:
                self.state = 641
                self.int_result(0)
                self.state = 642
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 643
                self.float_result(4)
                pass

            elif la_ == 3:
                self.state = 645
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 646
                self.float_result(0)
                self.state = 647
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 4:
                self.state = 649
                self.float_t()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 666
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 664
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.Float_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_result)
                        self.state = 652
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 653
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 654
                        self.float_result(9)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.Float_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_result)
                        self.state = 655
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 656
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 657
                        self.float_result(6)
                        pass

                    elif la_ == 3:
                        localctx = RubyParser.Float_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_result)
                        self.state = 658
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 659
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 660
                        self.int_result(0)
                        pass

                    elif la_ == 4:
                        localctx = RubyParser.Float_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_result)
                        self.state = 661
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 662
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 663
                        self.int_result(0)
                        pass

             
                self.state = 668
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class String_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def string_result(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.String_resultContext)
            else:
                return self.getTypedRuleContext(RubyParser.String_resultContext,i)


        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def literal_t(self):
            return self.getTypedRuleContext(RubyParser.Literal_tContext,0)


        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_string_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_result" ):
                listener.enterString_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_result" ):
                listener.exitString_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_result" ):
                return visitor.visitString_result(self)
            else:
                return visitor.visitChildren(self)



    def string_result(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.String_resultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_string_result, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.LEFT_RBRACKET, RubyParser.INT]:
                self.state = 670
                self.int_result(0)
                self.state = 671
                localctx.op = self.match(RubyParser.MUL)
                self.state = 672
                self.string_result(3)
                pass
            elif token in [RubyParser.LITERAL]:
                self.state = 674
                self.literal_t()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 685
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 683
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.String_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_string_result)
                        self.state = 677
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 678
                        localctx.op = self.match(RubyParser.PLUS)
                        self.state = 679
                        self.string_result(3)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.String_resultContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_string_result)
                        self.state = 680
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 681
                        localctx.op = self.match(RubyParser.MUL)
                        self.state = 682
                        self.int_result(0)
                        pass

             
                self.state = 687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comparison_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ComparisonContext
            self.op = None # Token
            self.right = None # Comparison_listContext

        def comparison(self):
            return self.getTypedRuleContext(RubyParser.ComparisonContext,0)


        def BIT_AND(self):
            return self.getToken(RubyParser.BIT_AND, 0)

        def comparison_list(self):
            return self.getTypedRuleContext(RubyParser.Comparison_listContext,0)


        def AND(self):
            return self.getToken(RubyParser.AND, 0)

        def BIT_OR(self):
            return self.getToken(RubyParser.BIT_OR, 0)

        def OR(self):
            return self.getToken(RubyParser.OR, 0)

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_comparison_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_list" ):
                listener.enterComparison_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_list" ):
                listener.exitComparison_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison_list" ):
                return visitor.visitComparison_list(self)
            else:
                return visitor.visitChildren(self)




    def comparison_list(self):

        localctx = RubyParser.Comparison_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_comparison_list)
        try:
            self.state = 709
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 688
                localctx.left = self.comparison()
                self.state = 689
                localctx.op = self.match(RubyParser.BIT_AND)
                self.state = 690
                localctx.right = self.comparison_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                localctx.left = self.comparison()
                self.state = 693
                localctx.op = self.match(RubyParser.AND)
                self.state = 694
                localctx.right = self.comparison_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 696
                localctx.left = self.comparison()
                self.state = 697
                localctx.op = self.match(RubyParser.BIT_OR)
                self.state = 698
                localctx.right = self.comparison_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 700
                localctx.left = self.comparison()
                self.state = 701
                localctx.op = self.match(RubyParser.OR)
                self.state = 702
                localctx.right = self.comparison_list()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 704
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 705
                self.comparison_list()
                self.state = 706
                self.match(RubyParser.RIGHT_RBRACKET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 708
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Comp_varContext
            self.op = None # Token
            self.right = None # Comp_varContext

        def comp_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.Comp_varContext)
            else:
                return self.getTypedRuleContext(RubyParser.Comp_varContext,i)


        def LESS(self):
            return self.getToken(RubyParser.LESS, 0)

        def GREATER(self):
            return self.getToken(RubyParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(RubyParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(RubyParser.GREATER_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(RubyParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(RubyParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = RubyParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.state = 719
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 711
                localctx.left = self.comp_var()
                self.state = 712
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.GREATER) | (1 << RubyParser.LESS) | (1 << RubyParser.LESS_EQUAL) | (1 << RubyParser.GREATER_EQUAL))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 713
                localctx.right = self.comp_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 715
                localctx.left = self.comp_var()
                self.state = 716
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==RubyParser.EQUAL or _la==RubyParser.NOT_EQUAL):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 717
                localctx.right = self.comp_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_result(self):
            return self.getTypedRuleContext(RubyParser.All_resultContext,0)


        def array_selector(self):
            return self.getTypedRuleContext(RubyParser.Array_selectorContext,0)


        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_comp_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_var" ):
                listener.enterComp_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_var" ):
                listener.exitComp_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_var" ):
                return visitor.visitComp_var(self)
            else:
                return visitor.visitChildren(self)




    def comp_var(self):

        localctx = RubyParser.Comp_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_comp_var)
        try:
            self.state = 724
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 721
                self.all_result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 722
                self.array_selector()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 723
                self.idd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idd(self):
            return self.getTypedRuleContext(RubyParser.IddContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = RubyParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
            self.idd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(RubyParser.LvalueContext,0)


        def initial_array_assignment(self):
            return self.getTypedRuleContext(RubyParser.Initial_array_assignmentContext,0)


        def array_assignment(self):
            return self.getTypedRuleContext(RubyParser.Array_assignmentContext,0)


        def int_result(self):
            return self.getTypedRuleContext(RubyParser.Int_resultContext,0)


        def float_result(self):
            return self.getTypedRuleContext(RubyParser.Float_resultContext,0)


        def string_result(self):
            return self.getTypedRuleContext(RubyParser.String_resultContext,0)


        def global_set(self):
            return self.getTypedRuleContext(RubyParser.Global_setContext,0)


        def global_get(self):
            return self.getTypedRuleContext(RubyParser.Global_getContext,0)


        def dynamic_assignment(self):
            return self.getTypedRuleContext(RubyParser.Dynamic_assignmentContext,0)


        def string_assignment(self):
            return self.getTypedRuleContext(RubyParser.String_assignmentContext,0)


        def float_assignment(self):
            return self.getTypedRuleContext(RubyParser.Float_assignmentContext,0)


        def int_assignment(self):
            return self.getTypedRuleContext(RubyParser.Int_assignmentContext,0)


        def assignment(self):
            return self.getTypedRuleContext(RubyParser.AssignmentContext,0)


        def function_call(self):
            return self.getTypedRuleContext(RubyParser.Function_callContext,0)


        def literal_t(self):
            return self.getTypedRuleContext(RubyParser.Literal_tContext,0)


        def bool_t(self):
            return self.getTypedRuleContext(RubyParser.Bool_tContext,0)


        def float_t(self):
            return self.getTypedRuleContext(RubyParser.Float_tContext,0)


        def int_t(self):
            return self.getTypedRuleContext(RubyParser.Int_tContext,0)


        def nil_t(self):
            return self.getTypedRuleContext(RubyParser.Nil_tContext,0)


        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RubyParser.RvalueContext)
            else:
                return self.getTypedRuleContext(RubyParser.RvalueContext,i)


        def NOT(self):
            return self.getToken(RubyParser.NOT, 0)

        def BIT_NOT(self):
            return self.getToken(RubyParser.BIT_NOT, 0)

        def LEFT_RBRACKET(self):
            return self.getToken(RubyParser.LEFT_RBRACKET, 0)

        def RIGHT_RBRACKET(self):
            return self.getToken(RubyParser.RIGHT_RBRACKET, 0)

        def EXP(self):
            return self.getToken(RubyParser.EXP, 0)

        def MUL(self):
            return self.getToken(RubyParser.MUL, 0)

        def DIV(self):
            return self.getToken(RubyParser.DIV, 0)

        def MOD(self):
            return self.getToken(RubyParser.MOD, 0)

        def PLUS(self):
            return self.getToken(RubyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RubyParser.MINUS, 0)

        def BIT_SHL(self):
            return self.getToken(RubyParser.BIT_SHL, 0)

        def BIT_SHR(self):
            return self.getToken(RubyParser.BIT_SHR, 0)

        def BIT_AND(self):
            return self.getToken(RubyParser.BIT_AND, 0)

        def BIT_OR(self):
            return self.getToken(RubyParser.BIT_OR, 0)

        def BIT_XOR(self):
            return self.getToken(RubyParser.BIT_XOR, 0)

        def LESS(self):
            return self.getToken(RubyParser.LESS, 0)

        def GREATER(self):
            return self.getToken(RubyParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(RubyParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(RubyParser.GREATER_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(RubyParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(RubyParser.NOT_EQUAL, 0)

        def OR(self):
            return self.getToken(RubyParser.OR, 0)

        def AND(self):
            return self.getToken(RubyParser.AND, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRvalue" ):
                return visitor.visitRvalue(self)
            else:
                return visitor.visitChildren(self)



    def rvalue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.RvalueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_rvalue, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 729
                self.lvalue()
                pass

            elif la_ == 2:
                self.state = 730
                self.initial_array_assignment()
                pass

            elif la_ == 3:
                self.state = 731
                self.array_assignment()
                pass

            elif la_ == 4:
                self.state = 732
                self.int_result(0)
                pass

            elif la_ == 5:
                self.state = 733
                self.float_result(0)
                pass

            elif la_ == 6:
                self.state = 734
                self.string_result(0)
                pass

            elif la_ == 7:
                self.state = 735
                self.global_set()
                pass

            elif la_ == 8:
                self.state = 736
                self.global_get()
                pass

            elif la_ == 9:
                self.state = 737
                self.dynamic_assignment()
                pass

            elif la_ == 10:
                self.state = 738
                self.string_assignment()
                pass

            elif la_ == 11:
                self.state = 739
                self.float_assignment()
                pass

            elif la_ == 12:
                self.state = 740
                self.int_assignment()
                pass

            elif la_ == 13:
                self.state = 741
                self.assignment()
                pass

            elif la_ == 14:
                self.state = 742
                self.function_call()
                pass

            elif la_ == 15:
                self.state = 743
                self.literal_t()
                pass

            elif la_ == 16:
                self.state = 744
                self.bool_t()
                pass

            elif la_ == 17:
                self.state = 745
                self.float_t()
                pass

            elif la_ == 18:
                self.state = 746
                self.int_t()
                pass

            elif la_ == 19:
                self.state = 747
                self.nil_t()
                pass

            elif la_ == 20:
                self.state = 748
                _la = self._input.LA(1)
                if not(_la==RubyParser.BIT_NOT or _la==RubyParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 749
                self.rvalue(10)
                pass

            elif la_ == 21:
                self.state = 750
                self.match(RubyParser.LEFT_RBRACKET)
                self.state = 751
                self.rvalue(0)
                self.state = 752
                self.match(RubyParser.RIGHT_RBRACKET)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 785
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 783
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 756
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 757
                        self.match(RubyParser.EXP)
                        self.state = 758
                        self.rvalue(12)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 759
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 760
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.MUL) | (1 << RubyParser.DIV) | (1 << RubyParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 761
                        self.rvalue(10)
                        pass

                    elif la_ == 3:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 762
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 763
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.PLUS or _la==RubyParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 764
                        self.rvalue(9)
                        pass

                    elif la_ == 4:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 765
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 766
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.BIT_SHL or _la==RubyParser.BIT_SHR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 767
                        self.rvalue(8)
                        pass

                    elif la_ == 5:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 768
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 769
                        self.match(RubyParser.BIT_AND)
                        self.state = 770
                        self.rvalue(7)
                        pass

                    elif la_ == 6:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 771
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 772
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.BIT_OR or _la==RubyParser.BIT_XOR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 773
                        self.rvalue(6)
                        pass

                    elif la_ == 7:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 774
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 775
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RubyParser.GREATER) | (1 << RubyParser.LESS) | (1 << RubyParser.LESS_EQUAL) | (1 << RubyParser.GREATER_EQUAL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 776
                        self.rvalue(5)
                        pass

                    elif la_ == 8:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 777
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 778
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.EQUAL or _la==RubyParser.NOT_EQUAL):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 779
                        self.rvalue(4)
                        pass

                    elif la_ == 9:
                        localctx = RubyParser.RvalueContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_rvalue)
                        self.state = 780
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 781
                        _la = self._input.LA(1)
                        if not(_la==RubyParser.AND or _la==RubyParser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 782
                        self.rvalue(3)
                        pass

             
                self.state = 787
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Break_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(RubyParser.BREAK, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_break_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_expression" ):
                listener.enterBreak_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_expression" ):
                listener.exitBreak_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_expression" ):
                return visitor.visitBreak_expression(self)
            else:
                return visitor.visitChildren(self)




    def break_expression(self):

        localctx = RubyParser.Break_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_break_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 788
            self.match(RubyParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(RubyParser.LITERAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_literal_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_t" ):
                listener.enterLiteral_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_t" ):
                listener.exitLiteral_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_t" ):
                return visitor.visitLiteral_t(self)
            else:
                return visitor.visitChildren(self)




    def literal_t(self):

        localctx = RubyParser.Literal_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_literal_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            self.match(RubyParser.LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(RubyParser.FLOAT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_float_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_t" ):
                listener.enterFloat_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_t" ):
                listener.exitFloat_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_t" ):
                return visitor.visitFloat_t(self)
            else:
                return visitor.visitChildren(self)




    def float_t(self):

        localctx = RubyParser.Float_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_float_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 792
            self.match(RubyParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RubyParser.INT, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_int_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_t" ):
                listener.enterInt_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_t" ):
                listener.exitInt_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_t" ):
                return visitor.visitInt_t(self)
            else:
                return visitor.visitChildren(self)




    def int_t(self):

        localctx = RubyParser.Int_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_int_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794
            self.match(RubyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RubyParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RubyParser.FALSE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_bool_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_t" ):
                listener.enterBool_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_t" ):
                listener.exitBool_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_t" ):
                return visitor.visitBool_t(self)
            else:
                return visitor.visitChildren(self)




    def bool_t(self):

        localctx = RubyParser.Bool_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_bool_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 796
            _la = self._input.LA(1)
            if not(_la==RubyParser.TRUE or _la==RubyParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nil_tContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(RubyParser.NIL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_nil_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil_t" ):
                listener.enterNil_t(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil_t" ):
                listener.exitNil_t(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_t" ):
                return visitor.visitNil_t(self)
            else:
                return visitor.visitChildren(self)




    def nil_t(self):

        localctx = RubyParser.Nil_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_nil_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 798
            self.match(RubyParser.NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IddContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RubyParser.ID, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_idd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdd" ):
                listener.enterIdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdd" ):
                listener.exitIdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdd" ):
                return visitor.visitIdd(self)
            else:
                return visitor.visitChildren(self)




    def idd(self):

        localctx = RubyParser.IddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_idd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            self.match(RubyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_globalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_GLOBAL(self):
            return self.getToken(RubyParser.ID_GLOBAL, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_id_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_global" ):
                listener.enterId_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_global" ):
                listener.exitId_global(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_global" ):
                return visitor.visitId_global(self)
            else:
                return visitor.visitChildren(self)




    def id_global(self):

        localctx = RubyParser.Id_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_id_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(RubyParser.ID_GLOBAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_FUNCTION(self):
            return self.getToken(RubyParser.ID_FUNCTION, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_id_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_function" ):
                listener.enterId_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_function" ):
                listener.exitId_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_function" ):
                return visitor.visitId_function(self)
            else:
                return visitor.visitChildren(self)




    def id_function(self):

        localctx = RubyParser.Id_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_id_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 804
            self.match(RubyParser.ID_FUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(RubyParser.SEMICOLON, 0)

        def crlf(self):
            return self.getTypedRuleContext(RubyParser.CrlfContext,0)


        def terminator(self):
            return self.getTypedRuleContext(RubyParser.TerminatorContext,0)


        def getRuleIndex(self):
            return RubyParser.RULE_terminator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminator" ):
                listener.enterTerminator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminator" ):
                listener.exitTerminator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminator" ):
                return visitor.visitTerminator(self)
            else:
                return visitor.visitChildren(self)



    def terminator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RubyParser.TerminatorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_terminator, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RubyParser.SEMICOLON]:
                self.state = 807
                self.match(RubyParser.SEMICOLON)
                pass
            elif token in [RubyParser.CRLF]:
                self.state = 808
                self.crlf()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 817
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 815
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                    if la_ == 1:
                        localctx = RubyParser.TerminatorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terminator)
                        self.state = 811
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 812
                        self.match(RubyParser.SEMICOLON)
                        pass

                    elif la_ == 2:
                        localctx = RubyParser.TerminatorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terminator)
                        self.state = 813
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 814
                        self.crlf()
                        pass

             
                self.state = 819
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Else_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(RubyParser.ELSE, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_else_token

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_token" ):
                listener.enterElse_token(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_token" ):
                listener.exitElse_token(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_token" ):
                return visitor.visitElse_token(self)
            else:
                return visitor.visitChildren(self)




    def else_token(self):

        localctx = RubyParser.Else_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_else_token)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
            self.match(RubyParser.ELSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CrlfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRLF(self):
            return self.getToken(RubyParser.CRLF, 0)

        def getRuleIndex(self):
            return RubyParser.RULE_crlf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrlf" ):
                listener.enterCrlf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrlf" ):
                listener.exitCrlf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrlf" ):
                return visitor.visitCrlf(self)
            else:
                return visitor.visitChildren(self)




    def crlf(self):

        localctx = RubyParser.CrlfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_crlf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
            self.match(RubyParser.CRLF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_list_sempred
        self._predicates[15] = self.function_definition_params_list_sempred
        self._predicates[20] = self.function_call_params_sempred
        self._predicates[34] = self.for_init_list_sempred
        self._predicates[37] = self.for_loop_list_sempred
        self._predicates[39] = self.statement_expression_list_sempred
        self._predicates[48] = self.array_definition_elements_sempred
        self._predicates[50] = self.dynamic_result_sempred
        self._predicates[52] = self.int_result_sempred
        self._predicates[53] = self.float_result_sempred
        self._predicates[54] = self.string_result_sempred
        self._predicates[59] = self.rvalue_sempred
        self._predicates[69] = self.terminator_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_list_sempred(self, localctx:Expression_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def function_definition_params_list_sempred(self, localctx:Function_definition_params_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def function_call_params_sempred(self, localctx:Function_call_paramsContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def for_init_list_sempred(self, localctx:For_init_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def for_loop_list_sempred(self, localctx:For_loop_listContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def statement_expression_list_sempred(self, localctx:Statement_expression_listContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def array_definition_elements_sempred(self, localctx:Array_definition_elementsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def dynamic_result_sempred(self, localctx:Dynamic_resultContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

    def int_result_sempred(self, localctx:Int_resultContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

    def float_result_sempred(self, localctx:Float_resultContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 3)
         

    def string_result_sempred(self, localctx:String_resultContext, predIndex:int):
            if predIndex == 22:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 4)
         

    def rvalue_sempred(self, localctx:RvalueContext, predIndex:int):
            if predIndex == 24:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 32:
                return self.precpred(self._ctx, 2)
         

    def terminator_sempred(self, localctx:TerminatorContext, predIndex:int):
            if predIndex == 33:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 34:
                return self.precpred(self._ctx, 3)
         




