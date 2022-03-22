# -----------------------------------------------------------------------------
# lexer.py
#
# Lexer para lenguaje LittleDuck2020
# -----------------------------------------------------------------------------
import ply.lex as lex

# Aqui definimos las palabras reservadas del lenguaje
keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
}

# Aqui enlistamos los tokens que el lexer estara manejando
tokens = [
          'LEFTBRACKET','RIGHTBRACKET',
          'LEFTPAREN', 'RIGHTPAREN',
          'GREATER', 'LESS', 'NOTEQUAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'ID', 'CTEI', 'CTEF',
          'COLON', 'SEMICOLON', 'COMMA', 'EQUALS', 'CTESTRING',
          'PROGRAM',
          'VAR', 'INT', 'FLOAT',
          'IF', 'ELSE',
          'PRINT'
          ]

# Definicion de las RegEx basicas que conforman el lenguaje
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_GREATER = r'>'
t_LESS = r'<'
t_NOTEQUAL = r'<>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_COLON = r':'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_EQUALS = r'\='
t_CTESTRING = r'\".*\"'
t_ignore = " \t"


# Definicion amplia de la RegEx a aceptar

# Definicion de ID
def t_ID(t):
    r'[A-za-z]([A-za-z]|[0-9])*'
    t.type = keywords.get(t.value, 'ID')
    return t


# Definicion de un flotante
def t_CTEF(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t


# Definicion de un entero
def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Definicion de una mas lineas nuevas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Definicion de un comentario
def t_comment(t):
    r'\//.*'
    pass

# Mensaje de error que el Lexer emitira
def t_error(t):
    print("Lexical error ' {0} ' found in line ' {1} ' ".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex()
