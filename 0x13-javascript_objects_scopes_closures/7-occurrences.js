#!/usr/bin/node

exports.nbOccurences = function nbOccurences (list, searchElement) {
  let count = 0;
  let counter = 0;

  while (list[counter] !== undefined) {
    if (list[counter] === searchElement) {
      count++;
    }
    counter++;
  }
  return count;
};
