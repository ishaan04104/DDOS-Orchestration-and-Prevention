const express = require('express');
const rateLimit = require('express-rate-limit');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
let requestNumber = 0;

const onRateLimitExceeded = (req, res, options) => {
    console.log(`Request ${requestNumber}: Too many requests from this IP...rejected due to suspicious amount of requests`);
    res.status(429).send('Too many requests...rejected due to suspicious amount of requests');
};

const limiter = rateLimit({
    windowMs: 60 * 1000,
    max: 10,
    message: 'Too many requests from this IP, please try again later.',
    handler: onRateLimitExceeded
});

app.use(limiter);
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
    requestNumber++;
    console.log(`Request ${requestNumber}: Email - ${email}, Password - ${password}`);
    res.sendFile(thanksFilePath);
});

const PORT = process.env.PORT || 3200;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});