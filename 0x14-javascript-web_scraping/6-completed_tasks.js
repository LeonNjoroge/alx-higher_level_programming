#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let m = 0; m < json.length; m++) {
      if (json[m].completed === true) {
        if (resp[json[m].userId] === undefined) {
          resp[json[m].userId] = 0;
        }
        resp[json[m].userId]++;
      }
    }
    console.log(resp);
  }
});
