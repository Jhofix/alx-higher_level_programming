#!/usr/bin/node

const file = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const content1 = file.readFileSync(file1);
const content2 = file.readFileSync(file2);

file.writeFile(file3, content1 + content2, (err) => {
  if (err) throw err;
});
