var express = require('express');
var router = express.Router();

router.get('/publicidad', function (req, res) {
    console.log('GET /publicidad');
    res.sendFile('index.html', { root: __dirname });
})
router.get('/turismo', function (req, res) {
    console.log('GET /turismo');
    res.sendFile('index2.html', { root: __dirname });
})
module.exports = router;