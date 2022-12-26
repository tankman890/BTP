const express = require('express');

const app = express();

var ids = new Set()

app.post('/grant_access/:rfid', (req, res) => {
  ids.add(req.params.rfid)
  res.end();
});

app.put('/revoke_access/:rfid', (req, res) => {
  ids.delete(req.params.rfid)
  res.end();
});

app.get('/', (req, res) => {
  const array = [];
  ids.forEach(v => array.push(v));
  res.json(JSON.stringify(array));
});

const PORT = process.env.PORT || 5070;

app.listen(PORT);

