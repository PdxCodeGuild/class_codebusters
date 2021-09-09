const header = document.querySelector('.header')
const bestClass = document.getElementById('best-class')
const header2 = document.querySelector('h2.header')
const content = document.querySelector('#content')
const colorButton = document.getElementById('change-color-button')



// const pokemon = [
//     {
//         id: 1,
//         name: 'bulbasaur',
//         type: 'grass'
//     },
//     {
//         id: 1,
//         name: 'bulbasaur',
//         type: 'grass'
//     },
//     {
//         id: 1,
//         name: 'bulbasaur',
//         type: 'grass'
//     }
// ]
// const nameInput = document.querySelector('main input')


const main = document.querySelector('main')
const nameInput = main.querySelector('input')
const nameButton = main.querySelector('button')

content.textContent = "TEST TEST TEST Overwritten with js"

main.innerHTML = '<img src="///picsum.photos/200" alt="random Image"/>'

// const oldHTML = document.body.innerHTML

// document.body.innerHTML = '🥸'

// setTimeout(function() {
//     document.body.innerHTML = oldHTML
// }, 5000)



bestClass.classList.add('fancy')
bestClass.classList.remove('fancy')

const faveColor = document.getElementById('fave-color')

faveColor.addEventListener('keypress', (event) => {
    if(event.key ==='Enter'){
        header2.style.color = color
    }
})
colorButton.addEventListener('click', () => {
    const color = faveColor.value
    header2.style.color = color
    faveColor.value= ''
})




async function getPokemon(){

    const response = await fetch("https://raw.githubusercontent.com/PdxCodeGuild/class_codebusters/main/3%20Django/labs/pokemon.json")

    const pokedex = await response.json()

    const tbody = document.getElementById('pokemon')

    for(pokemon of pokedex.pokemon){

        const tr = document.createElement('tr')
        const td1 = document.createElement('td')
        const td2 = document.createElement('td')
        const td3 = document.createElement('td')
        td1.textContent = pokemon.number
        td2.textContent = pokemon.name
        td3.textContent = pokemon.types.join(', ')
        
        
        tr.append(td1)
        tr.append(td2)
        tr.append(td3)
        tbody.append(tr)

    }
}

getPokemon()



const grandparent = document.getElementById('grandparent')
const parent = document.getElementById('parent')
const child = document.getElementById('child')
const problemChild = document.getElementById('problemChild')


grandparent.addEventListener('click', function(){
    console.log('clicked grandparent')
})
parent.addEventListener('click', function(){
    console.log('clicked parent')
})
child.addEventListener('click', function(){
    console.log('clicked child')
})
problemChild.addEventListener('click', function(event){
    event.stopPropagation()
    console.log('clicked problemChild')
})