#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a valid Movie ID as the first argument.');
  process.exit(1);
}

const timeoutInMilliseconds = 10 * 1000;
const url = `https://swapi.dev/api/films/${movieId}/`;

const options = {
  url,
  timeout: timeoutInMilliseconds
};

request(options, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Error: Received status code ${res.statusCode} from the API.`);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Function to fetch the character name from the character URL
    function getCharacterName (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    }

    // Fetch and print character names in order
    async function printCharacterNames () {
      for (const characterUrl of characters) {
        try {
          const characterName = await getCharacterName(characterUrl);
          console.log(characterName);
        } catch (err) {
          console.error(`Error fetching character data: ${err}`);
        }
      }
    }

    printCharacterNames();
  } catch (err) {
    console.error(`Error parsing JSON data: ${err}`);
  }
});
