
const fs = require('fs')
const readline = require('readline');

filename = process.argv[2];
tablename = process.argv[3];

async function processLineByLine() {
  const fileStream = fs.createReadStream(filename);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  for await (const line of rl) {
    const res = line.split(",")
    console.log(`INSERT INTO ${tablename} VALUES (${res[0]}, '${res[1]}');`);
  }
}

processLineByLine()
