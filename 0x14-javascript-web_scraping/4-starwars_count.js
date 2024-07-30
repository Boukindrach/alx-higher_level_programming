#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
  } else {
    try {
      const films = JSON.parse(body).results;
      const wedgeFilms = films.filter(film => 
        film.characters.includes(`${apiUrl}people/18/`)
      );
      console.log(wedgeFilms.length);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
