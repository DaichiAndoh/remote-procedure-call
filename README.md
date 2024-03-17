# remote-procedure-call &middot; ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=white)

クライアントプログラムがRPCを用いてサーバプログラムの関数を実行します。
クライアントプログラムは `Python` と `Node.js`、サーバプログラムは `Python` です。

また、クライアントプログラムとサーバプログラムは、UNIXドメインソケットを用いて通信します。

## Usage

1. サーバプログラム（`server/server.py`）を実行します。

```
$ cd server
$ python server.py
```

2. クライアントプログラム（`python_client/client.py` or `node_client/client.js`）を実行します。

**Pythonの場合**

```
$ cd python_client
$ python client.py
```

**Node.jsの場合**

```
$ cd node_client
$ node client.js
```
