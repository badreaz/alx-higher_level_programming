#!/usr/bin/node

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  let i = process.argv[2];
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
