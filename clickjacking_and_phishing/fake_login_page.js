const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

const formFilePath = path.join(__dirname, 'public', 'index.html');
const thanksFilePath = path.join(__dirname, 'public', 'thanks.html');

app.get('/', (req, res) => {
    res.sendFile(formFilePath);
});

app.post('/', (req, res) => {
    const { email, password } = req.body;
    console.log('Email:', email);
    console.log('Password:', password);
    res.sendFile(thanksFilePath);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});