let digimonData = {}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, {
        data: digimonData,
        onAutocomplete: function(el){
            getDigimon(el)
        }
    });
});


fetch('http://localhost:8000/digimon/all')
// .then(data => console.log(data))
.then(data => data.json())
.then(data => {
    for(let mon of data){
        digimonData[mon.name] = mon.img
    }
})


function getDigimon(mon){
    fetch('http://localhost:8000/digimon/'+mon)
    .then(data => data.json())
    .then(data => lazyShowDigimon(data))
}

function showDigimon(mon){
    const searchResult = document.getElementById('search-result')

    const name = document.createElement('h3')
    name.textContent = mon.name

    const img = document.createElement('img')
    img.src = mon.img
    img.alt = mon.name

    const level = document.createElement('p')
    level.textContent = mon.level

    searchResult.appendChild(name)
    searchResult.appendChild(img)
    searchResult.appendChild(level)

}


function lazyShowDigimon(mon){
    const searchResult = document.getElementById('search-result')
    
    
    searchResult.innerHTML = `
    <div class="row">
    <div class="col s12 m7">
    <div class="card">
    <div class="card-image">
    <img src="${mon.img}">
    <span class="card-title">${mon.name}</span>
    </div>
    <div class="card-content">
    <p>${mon.level}</p>
    </div>
    </div>
    </div>
    </div>
    `

}