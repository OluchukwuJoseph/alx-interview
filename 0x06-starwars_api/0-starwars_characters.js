#!/usr/bin/node

/**
 * This script prints all characters of a Star Wars movie
 */

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie.id>');
  process.exit(1);
}

const movieEndpoint = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function fetchData (endpoint) {
  return new Promise((resolve, reject) => {
    request(endpoint, (error, response, body) => {
      if (error) {
        reject(error); // Reject the promise if there is an error;
      } else if (response.statusCode !== 200) {
        reject(
          new Error(`Failed to load data from API, status code: ${response.statusCode}`)
        );
      }
      resolve(JSON.parse(body));
    });
  });
}

fetchData(movieEndpoint)
  .then(data => {
    const charactersData = data.characters.map(
      characterEndpoint => fetchData(characterEndpoint));

    return Promise.all(charactersData);
  })
  .then(charactersData => {
    for (const character of charactersData) {
      console.log(character.name);
    }
  });
