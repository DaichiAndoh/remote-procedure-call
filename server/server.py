from server_socket import ServerSocket
from data_processor import DataProcessor

# ソケット作成
server_socket = ServerSocket()

# クライアントからの接続待機
while True:
    try:
        # クライアントからの接続を受け入れ
        connection, client_address = server_socket.sock.accept()
        processor = DataProcessor(connection, client_address)

        # 指定された関数を実行
        print('processing...')
        processor.recieve_data_from_client()
        response_data = processor.execute_function()
        processor.send_data_to_client(response_data)

    except Exception as e:
        print(e)

    # 接続を閉じる
    finally:
        print('closing current connection')
        processor.connection.close()
