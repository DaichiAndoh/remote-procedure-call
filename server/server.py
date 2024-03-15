from server_socket import ServerSocket
from data_processor import DataProcessor

# ソケット作成
server_socket = ServerSocket('../socket/socket_file')

# クライアントからの接続待機
while True:
    # クライアントからの接続を受け入れ
    connection, client_address = server_socket.sock.accept()
    processor = DataProcessor(connection, client_address)

    # 指定された関数を実行
    try:
        while True:
            processor.recieve_data()

            if processor.all_data_received():
                processor.parse_recieved_data()
                response = processor.execute_function()
                processor.send_to_client(response)
                break

    # 接続を閉じる
    finally:
        print('closing current connection')
        connection.close()
