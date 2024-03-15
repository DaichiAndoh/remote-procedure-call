import socket
import sys
import json

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバに接続
try:
    server_address = '../socket/socket_file'
    print('connecting to {}'.format(server_address))
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

# サーバに接続できれば、サーバにメッセージを送信
try:
    # 実行する関数とその引数を標準入力から取得
    input_method = input('please input function name you want to execute: ')
    input_params = input('please input parameters separated by commas: ')
    input_data = {
        'method': input_method,
        'params': input_params.split(','),
    }
    input_data_json = json.dumps(input_data) + 'end\n'
    request_data = input_data_json.encode()

    # サーバへ送信
    sock.sendall(request_data)

    # サーバからの応答待機時間を2秒間に設定
    sock.settimeout(2)

    # サーバからの応答待機
    try:
        while True:
            # サーバからデータを受信
            # 最大32バイトのデータを読み込む
            data = sock.recv(32).decode('utf-8')

            if data:
                print('server response: ' + data)
            else:
                break

    # タイムアウトエラー時の処理
    except socket.timeout:
        print('socket timeout, ending listening for server messages')

# 接続を閉じる
finally:
    print('closing socket\n')
    sock.close()
