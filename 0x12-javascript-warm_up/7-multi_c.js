#!/usr/bin/node
const x = parseInt(process.argv);
  for (let i = 0; i < x; i++) {
if (IsNaN(x[i])) {
    console.log('Missing number of occurrences');
  }
} else {
    console.log('C is fun');
}
