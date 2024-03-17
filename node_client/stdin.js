const readline = require('readline');

class Stdin {
  constructor() {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
  }

  input(description) {
    return new Promise((resolve) => {
      this.rl.question(description, (inputedValue) => {
        resolve(inputedValue);
      });
    });
  }

  close() {
    this.rl.close();
  }
}

module.exports = Stdin;
