const net = require('node:net');

class ClientSocket {
  constructor(serverAddress = '../socket/socket_file') {
    this.serverAddress = serverAddress;
    this.socket = null;
  }

  async createSocket() {
    return new Promise((resolve, reject) => {
      const client = net.createConnection({ path: this.serverAddress }, () => {
        console.log('\nconnected to server');
        this.socket = client;
        resolve();
      });

      client.on('error', (err) => {
        reject(err);
      });
    });
  }

  async sendDataToServer(requestData) {
    return new Promise((resolve, reject) => {
      if (this.socket) {
        this.socket.write(requestData, 'utf-8', (err) => {
          if (err) reject(err);
          else resolve();
        });
      } else {
        reject(new Error('socket is not initialized'));
      }
    });
  }

  async receiveDataFromServer() {
    return new Promise((resolve, reject) => {
      if (this.socket) {
        let responseData = '';
  
        this.socket.on('data', (data) => {
          responseData += data.toString();
          if (responseData.indexOf('end\n') > -1) {
            responseData = responseData.replace('end\n', '');
            this.socket.end();
          }
        });
  
        this.socket.on('end', () => {
          console.log('disconnected from server');
          resolve(responseData);
        });
  
        this.socket.on('error', (err) => {
          reject(err);
        });
      } else {
        reject(new Error('socket is not initialized'));
      }
    });
  }
}

module.exports = ClientSocket;
