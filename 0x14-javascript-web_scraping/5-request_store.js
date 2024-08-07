#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const filePath = process.argv[3];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      }
    });
  }
});
