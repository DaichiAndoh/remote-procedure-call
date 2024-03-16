import socket
from errors import SocketInitializeFaildError, SocketNotInitializedError

class ClientSocket:
    def __init__(self, server_address = '../socket/socket_file'):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            print('\nconnecting to {}'.format(server_address))
            self.sock.connect(server_address)
        except socket.error as err:
            raise SocketInitializeFaildError()

    def send_data_to_server(self, request_data):
        if self.sock:
            self.sock.sendall(request_data)
            self.sock.settimeout(2)
        else:
            raise SocketNotInitializedError()

    def recieve_data_from_server(self):
        if self.sock:
            try:
                response_data = ''
                while True:
                    response_data += self.sock.recv(32).decode('utf-8')

                    if 'end\n' in response_data:
                        response_data = response_data.replace('end\n', '')
                        break

                return response_data

            except socket.timeout:
                print('socket timeout, ending listening for server messages')
                return ''
        
        raise SocketNotInitializedError()

    def close(self):
        if self.sock:
            print('closing current connection')
            self.sock.close()
        else:
            raise SocketNotInitializedError()
