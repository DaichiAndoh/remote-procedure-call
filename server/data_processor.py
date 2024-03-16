import json
from functions import func_hash_map
from validations import validate_func_name, validate_params

class DataProcessor:
    _func_hash_map = func_hash_map

    def __init__(self, connection, client_address):
        self.connection = connection
        self.client_address = client_address
        self.request_data_hash_map = {}
        print('\nconnection from', self.client_address)

    def recieve_data_from_client(self):
        request_data_str = ''
        while True:
            request_data = self.connection.recv(16)
            request_data_str += request_data.decode('utf-8')

            if 'end\n' in request_data_str:
                temp_json = request_data_str.replace('end\n', '')
                self.request_data_hash_map = json.loads(temp_json)
                break

    def execute_function(self):
        try:
            function_name = self.request_data_hash_map['function_name']
            params = self.request_data_hash_map['params']

            validate_func_name(function_name)
            validate_params(params)

            func = DataProcessor._func_hash_map[function_name]
            result = func(params[0], params[1])

            return str(result)

        except ValueError as e:
            return 'error: {}'.format(e)

        except Exception as e:
            print(e)
            return 'server error'

    def send_data_to_client(self, response_data):
        response_data += 'end\n'
        self.connection.sendall(response_data.encode('utf-8'))
