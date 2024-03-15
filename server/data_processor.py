import json
from functions import func_hash_map
from validations import validate_func_hash_map

class DataProcessor:
    _func_hash_map = func_hash_map
    _validate_func_hash_map = validate_func_hash_map

    def __init__(self, connection, client_address):
        self.connection = connection
        self.client_address = client_address
        self.recieved_data_json = ''
        self.recieved_data_hash_map = {}
        print('\nconnection from', self.client_address)

    def recieve_data(self):
        recieved_data = self.connection.recv(16)
        self.recieved_data_json += recieved_data.decode('utf-8')

    def all_data_received(self):
        return 'end\n' in self.recieved_data_json

    def parse_recieved_data(self):
        temp_json = self.recieved_data_json.replace('end\n', '')
        self.recieved_data_hash_map = json.loads(temp_json)

    def execute_function(self):
        try:
            method = self.recieved_data_hash_map['method']
            params = self.recieved_data_hash_map['params']

            DataProcessor._validate_func_hash_map['func_name'](method)

            func = DataProcessor._func_hash_map[method]
            validate_func = DataProcessor._validate_func_hash_map[method]
            result = func(validate_func(params))

            return str(result)

        except ValueError as e:
            return 'error: {}'.format(e)

        except Exception as e:
            return 'server error'

    def send_to_client(self, response):
        self.connection.sendall(response.encode('utf-8'))
