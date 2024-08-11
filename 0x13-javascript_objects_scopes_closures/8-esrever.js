#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let counter = list.length;

  for (counter; counter > 0; counter--) {
    revList[(revList.length - 1) + 1] = list[counter - 1];
  }
  return revList;
};
