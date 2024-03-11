#!/usr/bin/node

const argscount = process.argv.length - 2;
if (argscount === 0) {
	console.log('No argument');
} else if (argscount === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
