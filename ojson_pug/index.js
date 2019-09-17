let pug = require('pug')
let express = require('express')

let app = express()
app.listen(3000)


app.get('/',(req, res) => {
    let template = pug.compileFile('si.pug')
    res.send(template(require('./JC0.json')))
})