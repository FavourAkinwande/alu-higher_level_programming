#!/usr/bin/node
/*
Writing a script that writes a string to a file, which satisfies the following:
 -the first argument is the file path
 -the second argument is the string to write
 -the content of the file must be written in utf-8
 -if an error occurred during while writing, print the error object
*/
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (error) => {
  if (error) {
    console.log(error);
  }
});
