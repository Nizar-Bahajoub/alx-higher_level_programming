#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request (url, function (error, response, body) {
	if (error) {
		console.log(error);
		return;
	}

	data = JSON.parse(body);

	const completed = {};

	data.forEach((task) => {
		if (!task.completed) {
			return;
		}
		const userId = task.userId;

		if (completed[userId]) {
			completed[userId]++;
		} else {
			completed[userId] = 1;
		}
	});

	console.log(completed);
});
