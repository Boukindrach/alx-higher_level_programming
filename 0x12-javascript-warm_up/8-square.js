#!/usr/bin/node

if (process.argv.length === 2) {
	console.log('Missing size');
} else {
    if (!isNaN(parseFloat(process.argv[2])) && isFinite(process.argv[2])) {
	    for (let i = 0; i < process.argv[2]; i++) {
		    box = ''
		    for (let j = 0; j < process.argv[2]; j++) box += 'X';{
			    console.log(box);
		    }
	    }
     } else {
         console.log('Missing size');
  }
}
