#!/usr/bin/node

/**
 * This script prints all characters of a Star Wars movie
 */

const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(filmUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(`An error occured: ${error}`);
    return;
  }
  const characters = body.characters;
  printName(characters, 0);
});

/**
 * Prints the name of Characters in a List
 * @param list - List of characters
 * @param index - Start index
 * @return: Nothing
 */
function printName (list, index) {
  if (index === list.length) {
    return;
  }
  request(list[index], { json: true }, (error, response, body) => {
    if (error) {
      console.log(`An error occured: ${error}`);
      return;
    }
    console.log(body.name);
    printName(list, index + 1);
  });
}
