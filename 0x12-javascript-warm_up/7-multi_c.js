#!/usr/bin/node

const text = 'C is fun';
const errtext = 'Missing number of occurrences';

if (process.argv[2] > 0) {
  console.log(text);
} else if (isNaN(process.argv[2])) {
  console.log(errtext);
}
