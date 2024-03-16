from functions import Functions
from validations import validate_input_number

def main():
    try:
        num1 = None
        num2 = None

        while True:
            input_value = input('please input a number: ')
            if validate_input_number(input_value):
                if num1 is None:
                    num1 = float(input_value)
                else:
                    num2 = float(input_value)
                    break
            else:
                print('inputed value is not invalid. please input again.')

        functions = Functions()
        print('add result:', functions.add(num1, num2))
        print('minus result:', functions.minus(num1, num2))

        print('process end')

    except Exception as e:
        print('error occurred: {}'.format(e))

if __name__ == '__main__': 
    main() 
