class SocketInitializeFaildError(Exception):
    def __init__(self, message='Initialization of socket is faild.'):
        self.message = message
        super().__init__(self.message)

class SocketNotInitializedError(Exception):
    def __init__(self, message='Socket is not initialized.'):
        self.message = message
        super().__init__(self.message)
