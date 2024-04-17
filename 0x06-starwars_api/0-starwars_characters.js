#!/usr/bin/node
import request from 'request';

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  if (!filmData.characters || !filmData.characters.length) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  filmData.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character:', charError);
      } else if (charResponse.statusCode !== 200) {
        console.error('Unexpected status code for character:', charResponse.statusCode);
      } else {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      }
    });
  });
});
