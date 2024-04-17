#!/usr/bin/node

import request from 'request';

const id = process.argv[2] + '/';
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + id, async function (err, res, body) {
  if (err) return console.error(err);

  const listUrl = JSON.parse(body).characters;

  for (const li of listUrl) {
    await new Promise(function (resolve, reject) {
      request(li, function (err, res, body) {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});