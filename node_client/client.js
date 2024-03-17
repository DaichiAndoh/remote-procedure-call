const Functions = require('./functions');
const Stdin = require('./stdin');

async function main() {
  console.log('this program executes four arithmetic operations using two values inputed by you\n');

  try {
    let n1 = null;
    let n2 = null;

    while (true) {
      const stdin = new Stdin();
      const inputValue = await stdin.input('please input a number: ');
      if (!isNaN(inputValue)) {
        if (n1 === null) {
          n1 = Number(inputValue);
        }
        else {
          n2 = Number(inputValue);
          stdin.close();
          break;
        }
      } else {
        console.log('inputed value is not invalid. please input again');
      }
      stdin.close();
    }

    console.log(`\ninputed values are ${n1} and ${n2}`);
    console.log('execute four arithmetic operations');

    const functions = new Functions();
    console.log('add result:', await functions.add(n1, n2));
    console.log('minus result:', await functions.minus(n1, n2));
    console.log('multiply result:', await functions.multiply(n1, n2));
    console.log('divide result:', await functions.divide(n1, n2));
  } catch (error) {
    console.error(error);
  }
}

main().then(() => {
  console.log('\nprocess end');
});
