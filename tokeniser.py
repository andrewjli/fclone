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
annotation = Str("@") + identifier

lexicon = Lexicon([
    # Java keywords
    (Str("abstract"), "ABSTRACT"),
    (Str("assert"), "ASSERT"),
    (Str("boolean"), "TYPE_BOOLEAN"),
    (Str("break"), "BREAK"),
    (Str("byte"), "BYTE"),
    (Str("case"), "CASE"),
    (Str("catch"), "CATCH"),
    (Str("char"), "TYPE_CHAR"),
    (Str("class"), "CLASS"),
    (Str("const"), "CONST"),
    (Str("continue"), "CONTINUE"),
    (Str("default"), "DEFAULT"),
    (Str("do"), "DO"),
    (Str("double"), "DOUBLE"),
    (Str("else"), "ELSE"),
    (Str("enum"), "ENUM"),
    (Str("extends"), "EXTENDS"),
    (Str("final"), "FINAL"),
    (Str("finally"), "FINALLY"),
    (Str("float"), "TYPE_FLOAT"),
    (Str("for"), "FOR"),
    (Str("if"), "IF"),
    (Str("goto"), "GOTO"),
    (Str("implements"), "IMPLEMENTS"),
    (Str("import"), "IMPORT"),
    (Str("instanceof"), "INSTANCEOF"),
    (Str("int"), "TYPE_INT"),
    (Str("interface"), "INTERFACE"),
    (Str("long"), "LONG"),
    (Str("native"), "NATIVE"),
    (Str("new"), "NEW"),
    (Str("package"), "PACKAGE"),
    (Str("private"), "PRIVATE"),
    (Str("protected"), "PROTECTED"),
    (Str("public"), "PUBLIC"),
    (Str("return"), "RETURN"),
    (Str("short"), "SHORT"),
    (Str("static"), "STATIC"),
    (Str("strictfp"), "STRICTFP"),
    (Str("super"), "SUPER"),
    (Str("switch"), "SWITCH"),
    (Str("synchronized"), "SYNCHRONIZED"),
    (Str("this"), "THIS"),
    (Str("throw"), "THROW"),
    (Str("throws"), "THROWS"),
    (Str("transient"), "TRANSIENT"),
    (Str("try"), "TRY"),
    (Str("void"), "TYPE_VOID"),
    (Str("volatile"), "VOLATILE"),
    (Str("while"), "WHILE"),

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
    (identifier, "IDENTIFIER"),
    (decimal, "DECIMAL"),
    (integer, "INTEGER"),
    (annotation, "ANNOTATION"),
    (whitespace, IGNORE)
])

filename = "TOHprocessed.java"
f = open(filename, "r")
scanner = Scanner(lexicon, f, filename)
while 1:
    token = scanner.read()
    print token[0]
    if token[0] is None:
        break
