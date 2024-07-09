#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  try {
    const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
    let response = await request(endpoint);
    response = JSON.parse(response.body);
    const characters = response.characters;

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      let character = await request(urlCharacter);
      character = JSON.parse(character.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

starwarsCharacters(filmID);
