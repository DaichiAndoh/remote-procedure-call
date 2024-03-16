import math

def add(n1: int, n2: int):
    return math.floor(n1 + n2)

def minus(n1: int, n2: int):
    return math.floor(n1 - n2)

def multiply(n1: int, n2: int):
    return math.floor(n1 * n2)

def divide(n1: int, n2: int):
    return math.floor(n1 / n2)

func_hash_map = {
    'add': add,
    'minus': minus,
    'multiply': multiply,
    'divide': divide,
}
