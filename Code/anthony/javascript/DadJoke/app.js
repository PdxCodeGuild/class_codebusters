const jokeHeader = document.getElementById('joke')

console.log("Start of script")

// fetch('https://icanhazdadjoke.com/', {
//   headers: {
//     Accept: 'application/json'
//   }
// }).then(data => {
//   data.json()
//   .then(joke =>{
//     console.log(joke)
//     jokeHeader.innerText = joke.joke
//   })
// })


async function getJoke(){
  const data = await fetch('https://icanhazdadjoke.com/', {
      headers: {
        Accept: 'application/json'
      }
    })
  const joke = await data.json()
  jokeHeader.innerText = joke.joke
  console.log(joke)
}


window.addEventListener('load', getJoke)