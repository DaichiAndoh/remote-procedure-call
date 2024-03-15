import math

def floor(x: int):
    return math.floor(x)

def reverse(s: str):
    return s[::-1]

func_hash_map = {
    'floor': floor,
    'reverse': reverse,
}
