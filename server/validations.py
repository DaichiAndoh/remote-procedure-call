from functions import func_hash_map

def validate_func_name(func_name):
    if func_name not in func_hash_map:
        raise ValueError('function is not found')

def validate_floor_params(params):
    ERROR_MESSAGE = 'floor function requires one parameter which type is int or floor'
    if len(params) != 1:
        raise ValueError(ERROR_MESSAGE)

    try:
        return float(params[0])
    except ValueError:
        raise ValueError(ERROR_MESSAGE)

def validate_reverse_params(params):
    ERROR_MESSAGE = 'reverse function requires one parameter which type is str'
    if len(params) != 1:
        raise ValueError(ERROR_MESSAGE)

    if type(params[0]) != str:
        raise ValueError(ERROR_MESSAGE)

    return params[0]

validate_func_hash_map = {
    'func_name': validate_func_name,
    'floor': validate_floor_params,
    'reverse': validate_reverse_params,
}
