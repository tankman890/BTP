const express = require('express');
const fs = require('fs');

const app = express();

const fileName = './data.json';

app.post('/grant_access/:rfid', (req, res) => {
    const file = require(fileName);
    file.push(req.params.rfid);

    fs.writeFile(fileName, JSON.stringify(file), (err) => {});

    res.end();
});

app.put('/revoke_access/:rfid', (req, res) => {
    var file = require(fileName);
    file = file.filter((val) => { return val != req.params.rfid; })

    fs.writeFile(fileName, JSON.stringify(file), (err) => {});

    res.end();
});

app.get('/', (req, res) => {
    const file = require(fileName);
    res.json(JSON.stringify(file));
});

const PORT = process.env.PORT || 5070;

app.listen(PORT);

