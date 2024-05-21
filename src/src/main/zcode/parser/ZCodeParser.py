# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3y\n\3\3\4\3\4\5\4}\n\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6\u0085\n\6\3\7\3\7\5\7\u0089\n\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00a1\n\13\f\13")
        buf.write("\16\13\u00a4\13\13\3\f\3\f\3\r\3\r\5\r\u00aa\n\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\5\21\u00ba\n\21\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00c1\n\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00c9")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d3")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00df\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u00ea\n\32\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u00f1\n\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u00f9\n")
        buf.write("\34\f\34\16\34\u00fc\13\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u0104\n\35\f\35\16\35\u0107\13\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u010f\n\36\f\36\16\36\u0112\13")
        buf.write("\36\3\37\3\37\3\37\5\37\u0117\n\37\3 \3 \3 \5 \u011c\n")
        buf.write(" \3!\3!\3!\5!\u0121\n!\3!\3!\3!\5!\u0126\n!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u012f\n\"\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\5$\u013b\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0146")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3\'\3\'\5\'\u0150\n\'\3(\3(\3(\3")
        buf.write("(\3(\3(\5(\u0158\n(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3-\5-\u016e\n-\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3\60\3\60\5\60\u0179\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0180\n\61\3\62\3\62\3\62\3\62\5\62\u0186\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\5\64\u0190\n\64")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u0196\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u01ab\n\66\3\67\3\67\5")
        buf.write("\67\u01af\n\67\38\38\38\58\u01b4\n8\38\2\6\24\668:9\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\7\3\2\b\n\3\2\3\5\3")
        buf.write("\2\32\33\3\2\34\35\3\2\36 \2\u01ad\2p\3\2\2\2\4x\3\2\2")
        buf.write("\2\6|\3\2\2\2\b~\3\2\2\2\n\u0084\3\2\2\2\f\u0088\3\2\2")
        buf.write("\2\16\u008d\3\2\2\2\20\u0091\3\2\2\2\22\u0096\3\2\2\2")
        buf.write("\24\u009a\3\2\2\2\26\u00a5\3\2\2\2\30\u00a9\3\2\2\2\32")
        buf.write("\u00ab\3\2\2\2\34\u00ae\3\2\2\2\36\u00b3\3\2\2\2 \u00b9")
        buf.write("\3\2\2\2\"\u00c0\3\2\2\2$\u00c2\3\2\2\2&\u00c8\3\2\2\2")
        buf.write("(\u00d2\3\2\2\2*\u00d4\3\2\2\2,\u00de\3\2\2\2.\u00e0\3")
        buf.write("\2\2\2\60\u00e2\3\2\2\2\62\u00e9\3\2\2\2\64\u00f0\3\2")
        buf.write("\2\2\66\u00f2\3\2\2\28\u00fd\3\2\2\2:\u0108\3\2\2\2<\u0116")
        buf.write("\3\2\2\2>\u011b\3\2\2\2@\u0125\3\2\2\2B\u012e\3\2\2\2")
        buf.write("D\u0130\3\2\2\2F\u013a\3\2\2\2H\u0145\3\2\2\2J\u0147\3")
        buf.write("\2\2\2L\u014f\3\2\2\2N\u0157\3\2\2\2P\u0159\3\2\2\2R\u015d")
        buf.write("\3\2\2\2T\u0166\3\2\2\2V\u0168\3\2\2\2X\u016d\3\2\2\2")
        buf.write("Z\u016f\3\2\2\2\\\u0172\3\2\2\2^\u0178\3\2\2\2`\u017f")
        buf.write("\3\2\2\2b\u0185\3\2\2\2d\u0187\3\2\2\2f\u018f\3\2\2\2")
        buf.write("h\u0195\3\2\2\2j\u01aa\3\2\2\2l\u01ae\3\2\2\2n\u01b3\3")
        buf.write("\2\2\2pq\5l\67\2qr\5\4\3\2rs\7\2\2\3s\3\3\2\2\2tu\5\6")
        buf.write("\4\2uv\5\4\3\2vy\3\2\2\2wy\5\6\4\2xt\3\2\2\2xw\3\2\2\2")
        buf.write("y\5\3\2\2\2z}\5\b\5\2{}\5\34\17\2|z\3\2\2\2|{\3\2\2\2")
        buf.write("}\7\3\2\2\2~\177\5\n\6\2\177\u0080\5n8\2\u0080\t\3\2\2")
        buf.write("\2\u0081\u0085\5\f\7\2\u0082\u0085\5\16\b\2\u0083\u0085")
        buf.write("\5\20\t\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\13\3\2\2\2\u0086\u0089\5\26\f\2\u0087")
        buf.write("\u0089\7\r\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008b\7,\2\2\u008b\u008c\5")
        buf.write("\30\r\2\u008c\r\3\2\2\2\u008d\u008e\7\f\2\2\u008e\u008f")
        buf.write("\7,\2\2\u008f\u0090\5\32\16\2\u0090\17\3\2\2\2\u0091\u0092")
        buf.write("\5\26\f\2\u0092\u0093\7,\2\2\u0093\u0094\5\22\n\2\u0094")
        buf.write("\u0095\5\30\r\2\u0095\21\3\2\2\2\u0096\u0097\7$\2\2\u0097")
        buf.write("\u0098\5\24\13\2\u0098\u0099\7%\2\2\u0099\23\3\2\2\2\u009a")
        buf.write("\u009b\b\13\1\2\u009b\u009c\7\3\2\2\u009c\u00a2\3\2\2")
        buf.write("\2\u009d\u009e\f\3\2\2\u009e\u009f\7&\2\2\u009f\u00a1")
        buf.write("\7\3\2\2\u00a0\u009d\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\25\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6\27\3\2\2\2\u00a7")
        buf.write("\u00aa\5\32\16\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2")
        buf.write("\2\u00a9\u00a8\3\2\2\2\u00aa\31\3\2\2\2\u00ab\u00ac\7")
        buf.write("!\2\2\u00ac\u00ad\5\60\31\2\u00ad\33\3\2\2\2\u00ae\u00af")
        buf.write("\7\16\2\2\u00af\u00b0\7,\2\2\u00b0\u00b1\5\36\20\2\u00b1")
        buf.write("\u00b2\5(\25\2\u00b2\35\3\2\2\2\u00b3\u00b4\7\"\2\2\u00b4")
        buf.write("\u00b5\5 \21\2\u00b5\u00b6\7#\2\2\u00b6\37\3\2\2\2\u00b7")
        buf.write("\u00ba\5\"\22\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba!\3\2\2\2\u00bb\u00bc\5$\23")
        buf.write("\2\u00bc\u00bd\7&\2\2\u00bd\u00be\5\"\22\2\u00be\u00c1")
        buf.write("\3\2\2\2\u00bf\u00c1\5$\23\2\u00c0\u00bb\3\2\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1#\3\2\2\2\u00c2\u00c3\5\26\f\2\u00c3")
        buf.write("\u00c4\5&\24\2\u00c4%\3\2\2\2\u00c5\u00c9\7,\2\2\u00c6")
        buf.write("\u00c7\7,\2\2\u00c7\u00c9\5\22\n\2\u00c8\u00c5\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c9\'\3\2\2\2\u00ca\u00cb\5l\67")
        buf.write("\2\u00cb\u00cc\5d\63\2\u00cc\u00d3\3\2\2\2\u00cd\u00ce")
        buf.write("\5l\67\2\u00ce\u00cf\5X-\2\u00cf\u00d0\5n8\2\u00d0\u00d3")
        buf.write("\3\2\2\2\u00d1\u00d3\5n8\2\u00d2\u00ca\3\2\2\2\u00d2\u00cd")
        buf.write("\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3)\3\2\2\2\u00d4\u00d5")
        buf.write("\5,\27\2\u00d5\u00d6\7!\2\2\u00d6\u00d7\5\60\31\2\u00d7")
        buf.write("+\3\2\2\2\u00d8\u00df\7,\2\2\u00d9\u00da\7,\2\2\u00da")
        buf.write("\u00db\7$\2\2\u00db\u00dc\5F$\2\u00dc\u00dd\7%\2\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00d8\3\2\2\2\u00de\u00d9\3\2\2\2")
        buf.write("\u00df-\3\2\2\2\u00e0\u00e1\t\3\2\2\u00e1/\3\2\2\2\u00e2")
        buf.write("\u00e3\5\62\32\2\u00e3\61\3\2\2\2\u00e4\u00e5\5\64\33")
        buf.write("\2\u00e5\u00e6\7(\2\2\u00e6\u00e7\5\64\33\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00ea\5\64\33\2\u00e9\u00e4\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\63\3\2\2\2\u00eb\u00ec\5\66\34\2")
        buf.write("\u00ec\u00ed\7\'\2\2\u00ed\u00ee\5\66\34\2\u00ee\u00f1")
        buf.write("\3\2\2\2\u00ef\u00f1\5\66\34\2\u00f0\u00eb\3\2\2\2\u00f0")
        buf.write("\u00ef\3\2\2\2\u00f1\65\3\2\2\2\u00f2\u00f3\b\34\1\2\u00f3")
        buf.write("\u00f4\58\35\2\u00f4\u00fa\3\2\2\2\u00f5\u00f6\f\4\2\2")
        buf.write("\u00f6\u00f7\t\4\2\2\u00f7\u00f9\58\35\2\u00f8\u00f5\3")
        buf.write("\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\67\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe")
        buf.write("\b\35\1\2\u00fe\u00ff\5:\36\2\u00ff\u0105\3\2\2\2\u0100")
        buf.write("\u0101\f\4\2\2\u0101\u0102\t\5\2\2\u0102\u0104\5:\36\2")
        buf.write("\u0103\u0100\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0105\u0106\3\2\2\2\u01069\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u0109\b\36\1\2\u0109\u010a\5<\37\2\u010a")
        buf.write("\u0110\3\2\2\2\u010b\u010c\f\4\2\2\u010c\u010d\t\6\2\2")
        buf.write("\u010d\u010f\5<\37\2\u010e\u010b\3\2\2\2\u010f\u0112\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111;")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\7\31\2\2\u0114")
        buf.write("\u0117\5<\37\2\u0115\u0117\5> \2\u0116\u0113\3\2\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117=\3\2\2\2\u0118\u0119\7\35\2\2\u0119")
        buf.write("\u011c\5> \2\u011a\u011c\5@!\2\u011b\u0118\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c?\3\2\2\2\u011d\u0120\7$\2\2\u011e")
        buf.write("\u0121\5F$\2\u011f\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0126\7%\2\2")
        buf.write("\u0123\u0126\5D#\2\u0124\u0126\5B\"\2\u0125\u011d\3\2")
        buf.write("\2\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126A\3")
        buf.write("\2\2\2\u0127\u0128\7\"\2\2\u0128\u0129\5\60\31\2\u0129")
        buf.write("\u012a\7#\2\2\u012a\u012f\3\2\2\2\u012b\u012f\5.\30\2")
        buf.write("\u012c\u012f\7,\2\2\u012d\u012f\5Z.\2\u012e\u0127\3\2")
        buf.write("\2\2\u012e\u012b\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012d")
        buf.write("\3\2\2\2\u012fC\3\2\2\2\u0130\u0131\5B\"\2\u0131\u0132")
        buf.write("\7$\2\2\u0132\u0133\5F$\2\u0133\u0134\7%\2\2\u0134E\3")
        buf.write("\2\2\2\u0135\u013b\5\60\31\2\u0136\u0137\5\60\31\2\u0137")
        buf.write("\u0138\7&\2\2\u0138\u0139\5F$\2\u0139\u013b\3\2\2\2\u013a")
        buf.write("\u0135\3\2\2\2\u013a\u0136\3\2\2\2\u013bG\3\2\2\2\u013c")
        buf.write("\u013d\7\24\2\2\u013d\u013e\5J&\2\u013e\u013f\5L\'\2\u013f")
        buf.write("\u0146\3\2\2\2\u0140\u0141\7\24\2\2\u0141\u0142\5J&\2")
        buf.write("\u0142\u0143\5L\'\2\u0143\u0144\5P)\2\u0144\u0146\3\2")
        buf.write("\2\2\u0145\u013c\3\2\2\2\u0145\u0140\3\2\2\2\u0146I\3")
        buf.write("\2\2\2\u0147\u0148\7\"\2\2\u0148\u0149\5\60\31\2\u0149")
        buf.write("\u014a\7#\2\2\u014a\u014b\5l\67\2\u014b\u014c\5j\66\2")
        buf.write("\u014cK\3\2\2\2\u014d\u0150\5N(\2\u014e\u0150\3\2\2\2")
        buf.write("\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150M\3\2\2")
        buf.write("\2\u0151\u0152\7\26\2\2\u0152\u0153\5J&\2\u0153\u0154")
        buf.write("\5N(\2\u0154\u0158\3\2\2\2\u0155\u0156\7\26\2\2\u0156")
        buf.write("\u0158\5J&\2\u0157\u0151\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("O\3\2\2\2\u0159\u015a\7\25\2\2\u015a\u015b\5l\67\2\u015b")
        buf.write("\u015c\5j\66\2\u015cQ\3\2\2\2\u015d\u015e\7\17\2\2\u015e")
        buf.write("\u015f\7,\2\2\u015f\u0160\7\20\2\2\u0160\u0161\5\60\31")
        buf.write("\2\u0161\u0162\7\21\2\2\u0162\u0163\5\60\31\2\u0163\u0164")
        buf.write("\5l\67\2\u0164\u0165\5j\66\2\u0165S\3\2\2\2\u0166\u0167")
        buf.write("\7\22\2\2\u0167U\3\2\2\2\u0168\u0169\7\23\2\2\u0169W\3")
        buf.write("\2\2\2\u016a\u016e\7\13\2\2\u016b\u016c\7\13\2\2\u016c")
        buf.write("\u016e\5\60\31\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2")
        buf.write("\2\u016eY\3\2\2\2\u016f\u0170\7,\2\2\u0170\u0171\5\\/")
        buf.write("\2\u0171[\3\2\2\2\u0172\u0173\7\"\2\2\u0173\u0174\5^\60")
        buf.write("\2\u0174\u0175\7#\2\2\u0175]\3\2\2\2\u0176\u0179\5`\61")
        buf.write("\2\u0177\u0179\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179_\3\2\2\2\u017a\u017b\5b\62\2\u017b\u017c")
        buf.write("\7&\2\2\u017c\u017d\5`\61\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u0180\5b\62\2\u017f\u017a\3\2\2\2\u017f\u017e\3\2\2\2")
        buf.write("\u0180a\3\2\2\2\u0181\u0186\5\60\31\2\u0182\u0186\7,\2")
        buf.write("\2\u0183\u0184\7,\2\2\u0184\u0186\5b\62\2\u0185\u0181")
        buf.write("\3\2\2\2\u0185\u0182\3\2\2\2\u0185\u0183\3\2\2\2\u0186")
        buf.write("c\3\2\2\2\u0187\u0188\7\27\2\2\u0188\u0189\5n8\2\u0189")
        buf.write("\u018a\5f\64\2\u018a\u018b\7\30\2\2\u018b\u018c\5n8\2")
        buf.write("\u018ce\3\2\2\2\u018d\u0190\5h\65\2\u018e\u0190\3\2\2")
        buf.write("\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2\u0190g\3\2")
        buf.write("\2\2\u0191\u0192\5j\66\2\u0192\u0193\5h\65\2\u0193\u0196")
        buf.write("\3\2\2\2\u0194\u0196\5j\66\2\u0195\u0191\3\2\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196i\3\2\2\2\u0197\u0198\5*\26\2\u0198")
        buf.write("\u0199\5n8\2\u0199\u01ab\3\2\2\2\u019a\u01ab\5H%\2\u019b")
        buf.write("\u01ab\5R*\2\u019c\u019d\5T+\2\u019d\u019e\5n8\2\u019e")
        buf.write("\u01ab\3\2\2\2\u019f\u01a0\5V,\2\u01a0\u01a1\5n8\2\u01a1")
        buf.write("\u01ab\3\2\2\2\u01a2\u01a3\5Z.\2\u01a3\u01a4\5n8\2\u01a4")
        buf.write("\u01ab\3\2\2\2\u01a5\u01ab\5d\63\2\u01a6\u01a7\5X-\2\u01a7")
        buf.write("\u01a8\5n8\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\5\b\5\2\u01aa")
        buf.write("\u0197\3\2\2\2\u01aa\u019a\3\2\2\2\u01aa\u019b\3\2\2\2")
        buf.write("\u01aa\u019c\3\2\2\2\u01aa\u019f\3\2\2\2\u01aa\u01a2\3")
        buf.write("\2\2\2\u01aa\u01a5\3\2\2\2\u01aa\u01a6\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01abk\3\2\2\2\u01ac\u01af\5n8\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("m\3\2\2\2\u01b0\u01b1\7)\2\2\u01b1\u01b4\5n8\2\u01b2\u01b4")
        buf.write("\7)\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("o\3\2\2\2$x|\u0084\u0088\u00a2\u00a9\u00b9\u00c0\u00c8")
        buf.write("\u00d2\u00de\u00e9\u00f0\u00fa\u0105\u0110\u0116\u011b")
        buf.write("\u0120\u0125\u012e\u013a\u0145\u014f\u0157\u016d\u0178")
        buf.write("\u017f\u0185\u018f\u0195\u01aa\u01ae\u01b3")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<-'", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "'...'", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "NUMBERLIT", "BOOLLIT", "STRINGLIT", 
                      "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                      "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "ASSIGN", "LP", "RP", "LS", "RS", "COMMA", "RELOP", 
                      "CONCAT", "NEWLINE", "CMT", "WS", "IDENTIFIER", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_var_decl = 3
    RULE_var_decl_part = 4
    RULE_optional_vardecl = 5
    RULE_must_vardecl = 6
    RULE_arr_decl = 7
    RULE_arr_size_list = 8
    RULE_arr_size_prime = 9
    RULE_scalar_type = 10
    RULE_optional_initialize = 11
    RULE_initialize = 12
    RULE_func_decl = 13
    RULE_param_decl = 14
    RULE_param_list = 15
    RULE_param_prime = 16
    RULE_param = 17
    RULE_param_name = 18
    RULE_endfunc = 19
    RULE_assignstmt = 20
    RULE_lhs = 21
    RULE_literal = 22
    RULE_expr = 23
    RULE_expr1 = 24
    RULE_expr2 = 25
    RULE_expr3 = 26
    RULE_expr4 = 27
    RULE_expr5 = 28
    RULE_expr6 = 29
    RULE_expr7 = 30
    RULE_expr8 = 31
    RULE_expr9 = 32
    RULE_index_operation = 33
    RULE_index_operators = 34
    RULE_ifstmt = 35
    RULE_cond_block = 36
    RULE_optional_elif_list = 37
    RULE_optional_elif = 38
    RULE_optional_else = 39
    RULE_forstmt = 40
    RULE_breakstmt = 41
    RULE_continuestmt = 42
    RULE_returnstmt = 43
    RULE_callstmt = 44
    RULE_paramcall_part = 45
    RULE_paramcall_list = 46
    RULE_paramcall_prime = 47
    RULE_paramcall = 48
    RULE_blockstmt = 49
    RULE_stmt_list = 50
    RULE_stmt_prime = 51
    RULE_stmt = 52
    RULE_nullable_newline_list = 53
    RULE_newline_list = 54

    ruleNames =  [ "program", "decl_list", "decl", "var_decl", "var_decl_part", 
                   "optional_vardecl", "must_vardecl", "arr_decl", "arr_size_list", 
                   "arr_size_prime", "scalar_type", "optional_initialize", 
                   "initialize", "func_decl", "param_decl", "param_list", 
                   "param_prime", "param", "param_name", "endfunc", "assignstmt", 
                   "lhs", "literal", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "index_operation", "index_operators", "ifstmt", "cond_block", 
                   "optional_elif_list", "optional_elif", "optional_else", 
                   "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "paramcall_part", "paramcall_list", "paramcall_prime", 
                   "paramcall", "blockstmt", "stmt_list", "stmt_prime", 
                   "stmt", "nullable_newline_list", "newline_list" ]

    EOF = Token.EOF
    NUMBERLIT=1
    BOOLLIT=2
    STRINGLIT=3
    TRUE=4
    FALSE=5
    NUMBER=6
    BOOL=7
    STRING=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    NOT=23
    AND=24
    OR=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    MOD=30
    ASSIGN=31
    LP=32
    RP=33
    LS=34
    RS=35
    COMMA=36
    RELOP=37
    CONCAT=38
    NEWLINE=39
    CMT=40
    WS=41
    IDENTIFIER=42
    ERROR_CHAR=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.nullable_newline_list()
            self.state = 111
            self.decl_list()
            self.state = 112
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.decl()
                self.state = 115
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.func_decl()
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_part(self):
            return self.getTypedRuleContext(ZCodeParser.Var_decl_partContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.var_decl_part()
            self.state = 125
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_vardeclContext,0)


        def must_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Must_vardeclContext,0)


        def arr_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_part" ):
                return visitor.visitVar_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_part(self):

        localctx = ZCodeParser.Var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl_part)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.optional_vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.must_vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.arr_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def optional_initialize(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_initializeContext,0)


        def scalar_type(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_vardecl" ):
                return visitor.visitOptional_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def optional_vardecl(self):

        localctx = ZCodeParser.Optional_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optional_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 132
                self.scalar_type()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 133
                self.match(ZCodeParser.DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.optional_initialize()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Must_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def initialize(self):
            return self.getTypedRuleContext(ZCodeParser.InitializeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_must_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMust_vardecl" ):
                return visitor.visitMust_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def must_vardecl(self):

        localctx = ZCodeParser.Must_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_must_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.VAR)
            self.state = 140
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 141
            self.initialize()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_type(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_size_listContext,0)


        def optional_initialize(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_initializeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_decl" ):
                return visitor.visitArr_decl(self)
            else:
                return visitor.visitChildren(self)




    def arr_decl(self):

        localctx = ZCodeParser.Arr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.scalar_type()
            self.state = 144
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 145
            self.arr_size_list()
            self.state = 146
            self.optional_initialize()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def arr_size_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_size_primeContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_size_list" ):
                return visitor.visitArr_size_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_size_list(self):

        localctx = ZCodeParser.Arr_size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arr_size_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.LS)
            self.state = 149
            self.arr_size_prime(0)
            self.state = 150
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_size_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def arr_size_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_size_primeContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_size_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_size_prime" ):
                return visitor.visitArr_size_prime(self)
            else:
                return visitor.visitChildren(self)



    def arr_size_prime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Arr_size_primeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_arr_size_prime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.NUMBERLIT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Arr_size_primeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arr_size_prime)
                    self.state = 155
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 156
                    self.match(ZCodeParser.COMMA)
                    self.state = 157
                    self.match(ZCodeParser.NUMBERLIT) 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Scalar_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scalar_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_type" ):
                return visitor.visitScalar_type(self)
            else:
                return visitor.visitChildren(self)




    def scalar_type(self):

        localctx = ZCodeParser.Scalar_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scalar_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class Optional_initializeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initialize(self):
            return self.getTypedRuleContext(ZCodeParser.InitializeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_initialize

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_initialize" ):
                return visitor.visitOptional_initialize(self)
            else:
                return visitor.visitChildren(self)




    def optional_initialize(self):

        localctx = ZCodeParser.Optional_initializeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_optional_initialize)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.initialize()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

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


    class InitializeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initialize

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialize" ):
                return visitor.visitInitialize(self)
            else:
                return visitor.visitChildren(self)




    def initialize(self):

        localctx = ZCodeParser.InitializeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_initialize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.ASSIGN)
            self.state = 170
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def endfunc(self):
            return self.getTypedRuleContext(ZCodeParser.EndfuncContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.FUNC)
            self.state = 173
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self.param_decl()
            self.state = 175
            self.endfunc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ZCodeParser.LP)
            self.state = 178
            self.param_list()
            self.state = 179
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param_list)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.param_prime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_prime" ):
                return visitor.visitParam_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param_prime)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.param()
                self.state = 186
                self.match(ZCodeParser.COMMA)
                self.state = 187
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_type(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_typeContext,0)


        def param_name(self):
            return self.getTypedRuleContext(ZCodeParser.Param_nameContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.scalar_type()
            self.state = 193
            self.param_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr_size_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_size_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_name" ):
                return visitor.visitParam_name(self)
            else:
                return visitor.visitChildren(self)




    def param_name(self):

        localctx = ZCodeParser.Param_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_name)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 197
                self.arr_size_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_endfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndfunc" ):
                return visitor.visitEndfunc(self)
            else:
                return visitor.visitChildren(self)




    def endfunc(self):

        localctx = ZCodeParser.EndfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_endfunc)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.nullable_newline_list()
                self.state = 201
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.nullable_newline_list()
                self.state = 204
                self.returnstmt()
                self.state = 205
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.newline_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.lhs()
            self.state = 211
            self.match(ZCodeParser.ASSIGN)
            self.state = 212
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lhs)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 216
                self.match(ZCodeParser.LS)
                self.state = 217
                self.index_operators()
                self.state = 218
                self.match(ZCodeParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBERLIT) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.STRINGLIT))) != 0)):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Expr1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr1)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.expr2()
                self.state = 227
                self.match(ZCodeParser.CONCAT)
                self.state = 228
                self.expr2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr3Context,i)


        def RELOP(self):
            return self.getToken(ZCodeParser.RELOP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = ZCodeParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr2)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.expr3(0)
                self.state = 234
                self.match(ZCodeParser.RELOP)
                self.state = 235
                self.expr3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expr3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.expr4(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.expr5(0) 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.expr6() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr6)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(ZCodeParser.NOT)
                self.state = 274
                self.expr6()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr7)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(ZCodeParser.SUB)
                self.state = 279
                self.expr7()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expr8()
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def index_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operationContext,0)


        def expr9(self):
            return self.getTypedRuleContext(ZCodeParser.Expr9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr8)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(ZCodeParser.LS)
                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBERLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.IDENTIFIER]:
                    self.state = 284
                    self.index_operators()
                    pass
                elif token in [ZCodeParser.RS]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 288
                self.match(ZCodeParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.index_operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr9)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(ZCodeParser.LP)
                self.state = 294
                self.expr()
                self.state = 295
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.callstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(ZCodeParser.Expr9Context,0)


        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operation" ):
                return visitor.visitIndex_operation(self)
            else:
                return visitor.visitChildren(self)




    def index_operation(self):

        localctx = ZCodeParser.Index_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expr9()
            self.state = 303
            self.match(ZCodeParser.LS)
            self.state = 304
            self.index_operators()
            self.state = 305
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_index_operators)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.expr()
                self.state = 309
                self.match(ZCodeParser.COMMA)
                self.state = 310
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def cond_block(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_blockContext,0)


        def optional_elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_elif_listContext,0)


        def optional_else(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifstmt)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(ZCodeParser.IF)
                self.state = 315
                self.cond_block()
                self.state = 316
                self.optional_elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(ZCodeParser.IF)
                self.state = 319
                self.cond_block()
                self.state = 320
                self.optional_elif_list()
                self.state = 321
                self.optional_else()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_cond_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_block" ):
                return visitor.visitCond_block(self)
            else:
                return visitor.visitChildren(self)




    def cond_block(self):

        localctx = ZCodeParser.Cond_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_cond_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.LP)
            self.state = 326
            self.expr()
            self.state = 327
            self.match(ZCodeParser.RP)
            self.state = 328
            self.nullable_newline_list()
            self.state = 329
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_elifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_elif_list" ):
                return visitor.visitOptional_elif_list(self)
            else:
                return visitor.visitChildren(self)




    def optional_elif_list(self):

        localctx = ZCodeParser.Optional_elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_optional_elif_list)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.optional_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def cond_block(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_blockContext,0)


        def optional_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Optional_elifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_elif" ):
                return visitor.visitOptional_elif(self)
            else:
                return visitor.visitChildren(self)




    def optional_elif(self):

        localctx = ZCodeParser.Optional_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_optional_elif)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(ZCodeParser.ELIF)
                self.state = 336
                self.cond_block()
                self.state = 337
                self.optional_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(ZCodeParser.ELIF)
                self.state = 340
                self.cond_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_optional_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_else" ):
                return visitor.visitOptional_else(self)
            else:
                return visitor.visitChildren(self)




    def optional_else(self):

        localctx = ZCodeParser.Optional_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_optional_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.ELSE)
            self.state = 344
            self.nullable_newline_list()
            self.state = 345
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.FOR)
            self.state = 348
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 349
            self.match(ZCodeParser.UNTIL)
            self.state = 350
            self.expr()
            self.state = 351
            self.match(ZCodeParser.BY)
            self.state = 352
            self.expr()
            self.state = 353
            self.nullable_newline_list()
            self.state = 354
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_returnstmt)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(ZCodeParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(ZCodeParser.RETURN)
                self.state = 362
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramcall_part(self):
            return self.getTypedRuleContext(ZCodeParser.Paramcall_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 366
            self.paramcall_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramcall_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def paramcall_list(self):
            return self.getTypedRuleContext(ZCodeParser.Paramcall_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramcall_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamcall_part" ):
                return visitor.visitParamcall_part(self)
            else:
                return visitor.visitChildren(self)




    def paramcall_part(self):

        localctx = ZCodeParser.Paramcall_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_paramcall_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.LP)
            self.state = 369
            self.paramcall_list()
            self.state = 370
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramcall_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramcall_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Paramcall_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramcall_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamcall_list" ):
                return visitor.visitParamcall_list(self)
            else:
                return visitor.visitChildren(self)




    def paramcall_list(self):

        localctx = ZCodeParser.Paramcall_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_paramcall_list)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRINGLIT, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.paramcall_prime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Paramcall_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramcall(self):
            return self.getTypedRuleContext(ZCodeParser.ParamcallContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramcall_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Paramcall_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramcall_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamcall_prime" ):
                return visitor.visitParamcall_prime(self)
            else:
                return visitor.visitChildren(self)




    def paramcall_prime(self):

        localctx = ZCodeParser.Paramcall_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_paramcall_prime)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.paramcall()
                self.state = 377
                self.match(ZCodeParser.COMMA)
                self.state = 378
                self.paramcall_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.paramcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramcall(self):
            return self.getTypedRuleContext(ZCodeParser.ParamcallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamcall" ):
                return visitor.visitParamcall(self)
            else:
                return visitor.visitChildren(self)




    def paramcall(self):

        localctx = ZCodeParser.ParamcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_paramcall)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 386
                self.paramcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.BEGIN)
            self.state = 390
            self.newline_list()
            self.state = 391
            self.stmt_list()
            self.state = 392
            self.match(ZCodeParser.END)
            self.state = 393
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmt_list)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.stmt_prime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

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


    class Stmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_prime" ):
                return visitor.visitStmt_prime(self)
            else:
                return visitor.visitChildren(self)




    def stmt_prime(self):

        localctx = ZCodeParser.Stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt_prime)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.stmt()
                self.state = 400
                self.stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.assignstmt()
                self.state = 406
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.breakstmt()
                self.state = 411
                self.newline_list()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.continuestmt()
                self.state = 414
                self.newline_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 416
                self.callstmt()
                self.state = 417
                self.newline_list()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 419
                self.blockstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 420
                self.returnstmt()
                self.state = 421
                self.newline_list()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 423
                self.var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list" ):
                return visitor.visitNullable_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_nullable_newline_list)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.newline_list()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

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


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_newline_list)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(ZCodeParser.NEWLINE)
                self.state = 431
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(ZCodeParser.NEWLINE)
                pass


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
        self._predicates[9] = self.arr_size_prime_sempred
        self._predicates[26] = self.expr3_sempred
        self._predicates[27] = self.expr4_sempred
        self._predicates[28] = self.expr5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arr_size_prime_sempred(self, localctx:Arr_size_primeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




