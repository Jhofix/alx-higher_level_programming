#!/usr/bin/node

const text = 'C is fun';
const errtext = 'Missing number of occurrences';

if (process.argv[2] > 0) {
  let x = 0;
  while (x < process.argv[2]) {
    console.log(text);
    x++;
  }
} else if (isNaN(process.argv[2])) {
  console.log(errtext);
}
