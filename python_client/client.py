from functions import Functions
from validations import validate_input_number

def main():
    try:
        n1 = None
        n2 = None

        while True:
            input_value = input('please input a number: ')
            if validate_input_number(input_value):
                if n1 is None:
                    n1 = float(input_value)
                else:
                    n2 = float(input_value)
                    break
            else:
                print('inputed value is not invalid. please input again')

        print('\ninputed values are {} and {}'.format(n1, n2))

        functions = Functions()
        print('add result:', functions.add(n1, n2))
        print('minus result:', functions.minus(n1, n2))

        print('\nprocess end')

    except Exception as e:
        print('error occurred: {}'.format(e))

if __name__ == '__main__': 
    main() 
