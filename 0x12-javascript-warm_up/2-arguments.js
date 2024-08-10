#!/usr/bin/node
const args = process.argv;
const nArgs = 'No argument';
const oneArg = 'Argument found';
const moreArgs = 'Arguments found';

if (args.length < 3) {
  console.log(nArgs);
} else if (args.length === 3) {
  console.log(oneArg);
} else {
  console.log(moreArgs);
}
