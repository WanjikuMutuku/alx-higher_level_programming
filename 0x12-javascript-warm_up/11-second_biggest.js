#!/usr/bin/node

function secondBiggest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  return sortedNumbers[1] || 0;
}

const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg));

if (integers.length <= 1) {
  console.log(0);
} else {
  const result = secondBiggest(integers);
  console.log(result);
}
