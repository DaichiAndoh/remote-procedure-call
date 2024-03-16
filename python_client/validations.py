def validate_input_number(input_value):
    try:
        float(input_value)
        return True
    except ValueError:
        return False
