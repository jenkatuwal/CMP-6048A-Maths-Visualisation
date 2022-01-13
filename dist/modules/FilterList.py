RESERVED = 'RESERVED'
MATH_SHORT = 'MATH_SHORT'
OPERATOR = 'OPERATOR'
NUM = 'NUM'
ID = 'ID'

expressions = [
    # Program reserved symbols
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r';', RESERVED),
    (r',', RESERVED),
    (r':=', RESERVED),

    # Maths reserved words
    (r'frac', MATH_SHORT),
    (r'pow', MATH_SHORT),
    (r'sqrt', MATH_SHORT),
    (r'sin', MATH_SHORT),
    (r'cos', MATH_SHORT),
    (r'tan', MATH_SHORT),
    (r'pi', MATH_SHORT),

    # Maths reserved operators
    (r'\+', OPERATOR),
    (r'\+', OPERATOR),
    (r'-', OPERATOR),
    (r'\*', OPERATOR),
    (r'=', OPERATOR),
    (r'\(', OPERATOR),
    (r'\)', OPERATOR),

    # Non-Math Reserved
    (r'[+-]?([0-9]*[.])?[0-9]+', NUM),
    (r'[A-Za-z][A-Za-z0-9_]*', ID)
]
