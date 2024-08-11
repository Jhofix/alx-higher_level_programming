#!/usr/bin/node

const impList = require('./100-data.js').list;
const newList = impList.map((x, y) => (x * y));

console.log(impList);
console.log(newList);
