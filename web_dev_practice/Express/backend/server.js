console.log('H')
const express = require('express')
const app = express()
const cors = require("cors")
const coresOptions = {
    origin: ["http://localhost:5173"]
}

app.use(cors(coresOptions))

// Adding http method
app.get('/api', (req, res) => {
    console.log('here')
    res.status(200).json({ "fruits": ["orange", "banana", "apple"]})
    
})

app.listen(3000, ()=>
{
    console.log('server started')
}
)
//http://localhost:3000/api
