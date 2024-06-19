#!/usr/bin/node

const dict = require('./101-data').dict;
const groupValue = {};

for (const [key, value] of Object.entries(dict)) {
  if (!groupValue[value]) {
    groupValue[value] = [];
  }
  groupValue[value].push(key);
}

console.log(groupValue);
