#!/usr/bin/node

const request = require('request');
const StarWarsURL = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(StarWarsURL, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
