const express = require('express');

const fs = require('fs')

const app = express();

//var ids = new Set()

async function get_data() {
  const s = new Set();
  fs.readFile('data.txt', 'utf8', (err, data) => {
    if(err) {
      console.error(err);
      return;
    }

    const a = data.split(" ");

    for(const i of a) {
      console.log(i)
      s.add(i);
    }
  });

  return new Promise(resolve => {
    setTimeout(() => {resolve(s)}, 2000);
  });
}

function write(s) {
  let str = "";
  for(const i of s) {
    str = str + " " + i;
  }
  fs.writeFile('data.txt', str, err => {
    if(err) {
      console.error(err);
      return
    }
  })
}

app.post('/grant_access/:rfid', (req, res) => {
  //ids.add(req.params.rfid)
  const s = get_data();
  s.add(req.params.rfid);
  write(s);
  res.end();
});

app.put('/revoke_access/:rfid', (req, res) => {
  //ids.delete(req.params.rfid)
  const s = get_data();
  s.delete(req.params.rfid);
  write(s);
  res.end();
});

app.get('/', async (req, res) => {
  const array = [];
  const ids = await get_data();
  ids.forEach(v => array.push(v));
  console.log(array)
  console.log("what")
  res.json(JSON.stringify(array));
});

const PORT = process.env.PORT || 5070;

app.listen(PORT);

