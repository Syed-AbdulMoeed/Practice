console.log('H')
const express = require('express')
const app = express()

// Adding http method
app.get('/', (req, res) => {
    console.log('here')
    res.status(200).json({ "messsage": "bruh", "ere":123})
    
})

app.listen(3000)