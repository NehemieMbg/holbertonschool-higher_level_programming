#!/usr/bin/node

const link = process.argv[2];

const displayStatus = async function (url) {
  try {
    const response = await fetch(url);
    console.log(`code: ${response.status}`);
  } catch (err) {
    console.error(err);
  }
};

displayStatus(link);
