from functions import func_hash_map

def validate_func_name(func_name):
    if func_name not in func_hash_map:
        raise ValueError('function is not found')

def validate_params(params):
    ERROR_MESSAGE = 'params should be number list which length is two.'

    if len(params) != 2:
        raise ValueError(ERROR_MESSAGE)

    if type(params[0]) != float or type(params[1]) != float:
        raise ValueError(ERROR_MESSAGE)
