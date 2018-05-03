var fs = require('fs');


//get the last date for attempted quote
var lastDate = fs.readFileSync('./QTE.TXT').toString();
lastDate = lastDate.substr(lastDate.length-12, 12).trim();

//read the number of lines in the text file
var i;
var count = 0;
fs.createReadStream('./QTE.TXT')
  .on('data', function(chunk) {
    for (i=0; i < chunk.length; ++i)
      if (chunk[i] == 10) count++;
  })
  .on('end', function() {

    console.log('count: ', count);
    
    //generate json file once async has been resolved
    var fileContent = `{ 
        "quotesAttempted": ${count}, 
        "lastDate": "${lastDate}" }`
    var filepath = "data-huon.json";

    fs.writeFile(filepath, fileContent, (err) => {
        if(err) throw err;
        console.log("JSON successfully created!");
    });

  })





//display text
// fs.readFile('./QTE.TXT', function read(err,data)  {
//     if(err) throw err;
    
//      let strData = data.toString('utf-8');
//      strData = strData.substr(strData.length-12, 12).trim();
//      lastDate = strData;
//      return strData;
// });