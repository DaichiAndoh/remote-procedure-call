import json
from client_socket import ClientSocket

class Functions:
    def __init__(self):
        self.sock = None

    def _create_socket(self):
        if self.sock:
            self._close_socket()

        self.sock = ClientSocket()
    
    def _close_socket(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    def _craete_request_data(self, request_data_dict):
        request_data_str = json.dumps(request_data_dict) + 'end\n'
        return request_data_str.encode('utf-8')

    def _execute_function(self, function_name, n1, n2):
        self._create_socket()
        self.sock.send_data_to_server(
            self._craete_request_data({
                'function_name': function_name,
                'params': [n1, n2],
            })
        )
        response_data = self.sock.recieve_data_from_server()
        self._close_socket()
        return response_data

    def add(self, n1, n2):
        return self._execute_function('add', n1, n2)

    def minus(self, n1, n2):
        return self._execute_function('minus', n1, n2)

    def multiply(self, n1, n2):
        return self._execute_function('multiply', n1, n2)

    def divide(self, n1, n2):
        return self._execute_function('divide', n1, n2)
