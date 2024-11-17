#!/usr/bin/node

const request = require('request');

const req = (array, i) => {
	if (i === array.length) return;
	request(array[i], (error, response, body) => {
		if (error) {
			throw error;
		} else {
			console.log(JSON.parse(body).name);
			req(array, i + 1);
		}
	});
};
request(
	`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
	(error, response,  body) => {
	if (error){
	throw error;
	} else {
		const chars = JSON.parse(body).characters;
		req(chars, 0);
	}
});
