#!/usr/bin/node

const fs = require('fs');
const filea = fs.readFileSync(process.argv[2], 'utf-8');
const fileb = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], filea + fileb, 'utf-8');
