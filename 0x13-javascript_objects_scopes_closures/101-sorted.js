#!/usr/bin/node

const dict = require('./101-data').dict;
const newdict = {};
for (const k in dict) {
  if (!newdict[dict[k]]) {
    newdict[dict[k]] = [];
  }
  newdict[dict[k]].push(k);
}
console.log(newdict);
