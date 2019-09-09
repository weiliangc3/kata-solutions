const inquirer = require("inquirer");

const ask = async () => {
  return inquirer.prompt({
    name: 'askParameter',
    type: "input",
    message: "Input something:"
  })
}
async function main() {
  const input = await ask();

  console.log(`you input ${input.askParameter}`)
}

main();
