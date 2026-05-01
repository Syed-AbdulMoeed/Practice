function update(player, button) {
    let nplayer = document.getElementById('player')
    nplayer.innerHTML = player

    for (let i = 0; i < 3; ++i) {
        buttons[i].innerHTML = data[player][i]
    }
    console.log('test')
}


const data = {
    'Faker': ['Gumayusi', 'Zeus', 'Canna'],
    'Canna' : ['test', 'test', 'test'],
    'Zeus' : ['test', 'test', 'test'],
    'Gumayusi' : ['test', 'test', 'test'],
    'test' : ['Faker','Faker','Faker']
}



var buttons = document.querySelectorAll('.mate')

buttons.forEach(button => {
    button.addEventListener('click', () => {
        update(button.innerHTML, button)
    })     
})