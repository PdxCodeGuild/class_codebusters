const header1 = document.querySelector('.header')
const bestClass = document.getElementById('best-class')
const header2 = document.querySelector('h2.header')
const content = document.querySelector('#content')

// const nameInput = document.querySelector('main input')

const main = document.querySelector('main')

const nameInput = main.querySelector('input')
const nameButton = main.querySelector('button')


content.textContent = "Those who sleep with itchy butt, wake with stinky fingers"

main.innerHTML = '<img src="///picsum.photos/200" alt="random image"/>'

// const oldHTML = document.body.innerHTML

// document.body.innerHTML = '😎'

// setTimeout(function() {
//   document.body.innerHTML = oldHTML
// }, 5000)

header1.style.backgroundColor = 'cyan'

bestClass.classList.add('fancy')
bestClass.classList.remove('fancy')
bestClass.classList.toggle('fancy')
bestClass.classList.add('fancy')
bestClass.classList.add('fancy')
bestClass.classList.add('fancy')



const favColor = document.getElementById('fav-color')
const colorBtn = document.getElementById('change-color-btn')

favColor.addEventListener('keypress', (event) => {
  if(event.key === 'Enter'){
    const color = favColor.value
    header1.style.color = color
    favColor.value = ''
  }
})
colorBtn.addEventListener('click', () => {
  const color = favColor.value
  header1.style.color = color
  favColor.value = ''
})

async function getPokemon(){

  const response = await fetch('https://raw.githubusercontent.com/PdxCodeGuild/class_codebusters/main/3%20Django/labs/pokemon.json')

  const pokedex = await response.json()
  // console.log(pokedex)

  const tbody = document.getElementById('pokemon')

  for(pokemon of pokedex.pokemon){
    const tr = document.createElement('tr')
    const td1 = document.createElement('td')
    const td2 = document.createElement('td')
    const td3 = document.createElement('td')

    // console.log(pokemon)

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
  console.log('Clicked the grandparent')
})

parent.addEventListener('click', function(){
  console.log('Clicked the parent')
})

child.addEventListener('click', function(){
  console.log('Clicked the child')
})

problemChild.addEventListener('click', function(event){
  event.stopPropagation()
  console.log('Clicked the problemChild')
})