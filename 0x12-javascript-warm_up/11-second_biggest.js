#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const num = process.argv.slice(2).map(Number);
  console.log(num.sort((a, b) => b - a)[1]);
}
