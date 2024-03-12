#!/usr/bin/node
const dict = require('./101-data').dict;
const dKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};

// loops over the values
for (let m = 0; m < values.length; m++) {
  result[JSON.stringify(values[m])] = [];
  matched = dKeys.filter(key => dict[key] === values[m]);
  matched.forEach(item => result[JSON.stringify(values[m])].push(item));
}
console.log(result);
