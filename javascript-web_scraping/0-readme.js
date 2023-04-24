#!/usr/bin/node

const fs = require('fs');
const file = process.argv[0];

fs.readFile(file, 'utf-8', function(err, data) {
	if (err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
