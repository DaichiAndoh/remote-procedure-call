import os
import socket

class ServerSocket:
    def __init__(self, server_address):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            os.unlink(server_address)
        except FileNotFoundError:
            pass

        print('starting up on {}'.format(server_address))
        self.sock.bind(server_address)
        self.sock.listen(1)
