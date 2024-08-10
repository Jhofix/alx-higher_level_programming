#!/usr/bin/node

const text = 'C is fun';
const errtext = 'Missing number of occurrences';

if (process.argv[2] > 0) {
  console.log(text);
} else {
    if (process.argv[2] <= 0) {
      return;
    }
    console.log(errtext);
}