const ClientSocket = require('./client_socket');

class Functions {
  _craeteRequestData(requestDataObj) {
    return JSON.stringify(requestDataObj) + 'end\n';
  }

  async _executeFunction(functionName, n1, n2) {
    const requestData = this._craeteRequestData({
      function_name: functionName,
      params: [n1, n2],
    });

    const clientSocket = new ClientSocket();
    await clientSocket.createSocket();
    await clientSocket.sendDataToServer(requestData);
    return await clientSocket.receiveDataFromServer();
  }

  async add(n1, n2) {
    return await this._executeFunction('add', n1, n2)
  }

  async minus(n1, n2) {
    return await this._executeFunction('minus', n1, n2) 
  }

  async multiply(n1, n2) {
    return await this._executeFunction('multiply', n1, n2) 
  }

  async divide(n1, n2) {
    return await this._executeFunction('divide', n1, n2) 
  }
}

module.exports = Functions;
