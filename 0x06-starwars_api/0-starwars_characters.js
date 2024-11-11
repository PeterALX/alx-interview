#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Error! You need to provide a film id');
  process.exit(1);
}
if (isNaN(process.argv[2])) {
  console.error('Error! please provide a number as the film Id');
  process.exit(1);
}

const filmId = Number(process.argv[2]);
request(`https://swapi-api.alx-tools.com/api/films/${filmId}/`, async function (err, res, body) {
  if (err) {
    console.error('Error fetching film data');
    process.exit(1);
  }
  const characterUrls = JSON.parse(body).characters;
  const characterNames = Array(characterUrls.length);
  characterUrls.forEach((url, index) => {
    request(url,
      async function (err, res, body) {
        if (err) {
          console.error(`Error fetching ${url}`);
          process.exit(1);
        }
        characterNames[index] = JSON.parse(body).name;
        if (!characterNames.includes(undefined)) {
          characterNames.forEach(name => {
            console.log(name);
          });
        }
      });
  });
});
