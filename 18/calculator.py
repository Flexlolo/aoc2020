from typing import Tuple

OPERATIONS = { \
    "+": (lambda x, y: x + y), \
    "-": (lambda x, y: x - y), \
    "*": (lambda x, y: x * y), \
}

Expr = Tuple

def calculator(expr):
    if isinstance(expr, tuple):
        return OPERATIONS[expr[1]](calculator(expr[0]), calculator(expr[2]))

    return expr

def parse(expr: str) -> Expr
	
print(calculator(((1, '+', 2), '*', 3)))
# TODO