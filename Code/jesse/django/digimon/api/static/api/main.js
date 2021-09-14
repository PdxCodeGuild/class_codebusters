let digimonData = {};

document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".autocomplete");
  var instances = M.Autocomplete.init(elems, {
    data: digimonData,
    onAutocomplete: function (el) {
      getDigimon(el);
    },
  });
});

function getDigimon(mon) {
  fetch(`http://localhost:8000/digimon/${mon}`)
    .then((data) => data.json())
    .then((data) => {
      lazyShowDigimon(data);
    });
}

function lazyShowDigimon(mon) {
  const searchResult = document.getElementById("search-result");

  searchResult.innerHTML = `
    <div class="row">
      <div class="col s12 m6 l4">
        <div class="card">
          <div class="card-image">
            <img src="${mon.img}">
            <span class="card-title teal-text">${mon.name}</span>
          </div>
          <div class="card-content blue lighten-3">
            <p>${mon.level}</p>
          </div>
        </div>
      </div>
    </div>
`;
}

function showDigimon(mon) {
  const searchResult = document.getElementById("search-result");

  searchResult.innerHTML = "";

  const name = document.createElement("h3");
  name.textContent = mon.name;
  const img = document.createElement("img");
  img.src = mon.img;
  img.alt = mon.name;
  const level = document.createElement("p");
  level.textContent = mon.level;

  searchResult.appendChild(name);
  searchResult.appendChild(img);
  searchResult.appendChild(level);
}

fetch("http://localhost:8000/digimon/all")
  .then((data) => data.json())
  .then((data) => {
    console.log(data);
    for (let mon of data) {
      digimonData[mon.name] = mon.img;
    }
  });
