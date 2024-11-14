#!/usr/bin/node

/**
 * This script prints all characters of a Star Wars movie
 */

const request = require('request');

const filmEndpoint = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(filmEndpoint, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (const characterEndpoint of body.characters) {
      request(characterEndpoint, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        body = JSON.parse(body);
        console.log(body.name);
      });
    }
  }
});
