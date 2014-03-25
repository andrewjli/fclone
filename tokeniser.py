import sys
from plex import *

whitespace = Any(" \t\r\n\f")

digit = Range("09")
number = (Range("19") + Rep(digit)) | Str("0")
negative = Str("-") | Empty
integer = negative + number
decimal = negative + number + Str(".") + Rep(digit)

letter = Range("AZaz")
javaletter = letter | Str("_") | Str("$")
char = letter | digit | whitespace
character = Str("\'") + char + Str("\'")
string = Str("\"") + Rep(char) + Str("\"")
identifier = javaletter + Rep(javaletter|digit)

emptyfunction = identifier + Str("()")
annotation = Str("@") + identifier + Opt(Str("(\"") + identifier + Str("\")"))

lexicon = Lexicon([
    # Java keywords
    (Str("abstract"), "ABSTRACT"),
    (Str("assert"), "ASSERT"),
    (Str("break"), "BREAK"),
    (Str("case"), "CASE"),
    (Str("catch"), "CATCH"),
    (Str("class"), "CLASS"),
    (Str("continue"), "CONTINUE"),
    (Str("default"), "DEFAULT"),
    (Str("do"), "DO"),
    (Str("else"), "ELSE"),
    (Str("extends"), "EXTENDS"),
    (Str("finally"), "FINALLY"),
    (Str("for"), "FOR"),
    (Str("if"), "IF"),
    (Str("implements"), "IMPLEMENTS"),
    (Str("import"), "IMPORT"),
    (Str("instanceof"), "INSTANCEOF"),
    (Str("interface"), "INTERFACE"),
    (Str("native"), "NATIVE"),
    (Str("new"), "NEW"),
    (Str("package"), "PACKAGE"),
    (Str("return"), "RETURN"),
    (Str("static"), "STATIC"),
    (Str("strictfp"), "STRICTFP"),
    (Str("super"), "SUPER"),
    (Str("switch"), "SWITCH"),
    (Str("synchronized"), "SYNCHRONIZED"),
    (Str("transient"), "TRANSIENT"),
    (Str("this"), "THIS"),
    (Str("throw"), "THROW"),
    (Str("throws"), "THROWS"),
    (Str("try"), "TRY"),
    (Str("volatile"), "VOLATILE"),
    (Str("while"), "WHILE"),

    # Unneeded?
    (Str("final"), IGNORE),
    (Str("private"), IGNORE),
    (Str("protected"), IGNORE),
    (Str("public"), IGNORE),

    # Unused keywords
    (Str("const"), IGNORE),
    (Str("goto"), IGNORE),

    # Types
    (Str("boolean"), "TYPE_BOOLEAN"),
    (Str("byte"), "TYPE_STRING"),
    (Str("char"), "TYPE_STRING"),
    (Str("double"), "TYPE_NUMERICAL"),
    (Str("enum"), "TYPE_NUMERICAL"),
    (Str("float"), "TYPE_NUMERICAL"),
    (Str("int"), "TYPE_NUMERICAL"),
    (Str("long"), "TYPE_NUMERICAL"),
    (Str("short"), "TYPE_NUMERICAL"),

    (Str("void"), "TYPE_VOID"),

    # Boolean literals
    (Str("true"), "TRUE"),
    (Str("false"), "FALSE"),

    # Null literal
    (Str("null"), "NULL"),

    # Separators
    (Str("\'"), "APOSTROPHE"),
    (Str("\""), "QUOTEMARK"),
    (Str(";"), "SEMI"),
    (Str(","), "COMMA"),
    (Str("."), "PERIOD"),
    (Str("("), "LPAREN"),
    (Str(")"), "RPAREN"),
    (Str("["), "LBRACKET"),
    (Str("]"), "RBRACKET"),
    (Str("{"), "LBRACE"),
    (Str("}"), "RBRACE"),

    # Operators
    (Str("="), "ASSIGN"),           # Assignment operator
    (Str(">"), "GREATERTHAN"),
    (Str("<"), "LESSTHAN"),
    (Str("!"), "COMPLEMENT"),
    (Str("~"), "B_COMPLEMENT"),     # Bitwise complement
    (Str("?"), "TERNARY"),
    (Str(":"), "COLON"),            # Technically part of ternary operator
    (Str("=="), "EQUALTO"),
    (Str("<="), "LESSTHAN_EQUALTO"),
    (Str(">="), "GREATERTHAN_EQUALTO"),
    (Str("!="), "NOT_EQUALTO"),
    (Str("&&"), "AND"),
    (Str("||"), "OR"),
    (Str("++"), "INCREMENT"),
    (Str("--"), "DECREMENT"),
    (Str("+"), "PLUS"),
    (Str("-"), "MINUS"),
    (Str("*"), "TIMES"),
    (Str("/"), "DIVIDE"),
    (Str("&"), "B_AND"),            # Bitwise AND
    (Str("|"), "B_OR"),             # Bitwise OR
    (Str("^"), "B_XOR"),            # Bitwise XOR
    (Str("%"), "REMAINDER"),
    (Str("<<"), "B_LEFTSHIFT"),     # Bitwise Signed Left Shift
    (Str(">>"), "B_RIGHTSHIFT"),    # Bitwise Signed Right Shift
    (Str(">>>"), "B_U_RIGHTSHIFT"), # Bitwise Unsigned Right Shift
    (Str("@"), "AT"),

    # Compound Assignment Operators
    (Str("+="), "ASSIGN_PLUS"),
    (Str("-="), "ASSIGN_MINUS"),
    (Str("*="), "ASSIGN_TIMES"),
    (Str("/="), "ASSIGN_DIVIDE"),
    (Str("&="), "ASSIGN_AND"),
    (Str("|="), "ASSIGN_OR"),
    (Str("^="), "ASSIGN_XOR"),
    (Str("%="), "ASSIGN_REMAINDER"),
    (Str("<<="), "ASSIGN_B_LEFTSHIFT"),
    (Str(">>="), "ASSIGN_B_RIGHTSHIFT"),
    (Str(">>>="), "ASSIGN_B_U_RIGHTSHIFT"),

    # Identifiers, numbers, etc.
    (identifier, "STRING"),
    (decimal, "NUMERIC"),
    (integer, "NUMERIC"),
    (annotation, "ANNOTATION"),
    (emptyfunction, "FUNCTION"),
    (whitespace, IGNORE)
])


def tokenise(name):
    f = open(name, "r")
    scanner = Scanner(lexicon, f, name)

    #print name[:-1]
    g = open(name[:-1] + "t", "w")
    while 1:
        token = scanner.read()
        g.write(str(token[0]))
        g.write("\n")
        if token[0] is None:
            f.close()
            g.close()
            break
