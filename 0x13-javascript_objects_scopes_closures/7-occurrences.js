#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occNum = 0;
  for (const i of list) {
    if (i === searchElement) {
      occNum++;
    }
  }
  return occNum;
};
