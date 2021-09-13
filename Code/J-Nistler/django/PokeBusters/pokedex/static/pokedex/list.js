//JS code for the list generation and rendering

const poke_card_img = document.getElementById("poke_card_img")
const poke_card_name = document.getElementById("poke_card_name")
const poke_card_number = document.getElementById("poke_card_number")
const poke_card_weight = document.getElementById("poke_card_weight")
const poke_card_height = document.getElementById("poke_card_height")

let POKE = [];

function getPoke() {
  fetch(`http://localhost:8000/all_pokemon`)
    .then((data) => data.json())
    .then((data) => {
      renderList(buildData(data));
    });
}

function buildData(data) {
  for (let poke of data) {
    let dict = {}
    let type = []
    dict["poke_id"] = poke.number
    dict["poke_name"] = poke.name;
    dict["poke_height"] = poke.height;
    dict["poke_weight"] = poke.weight;
    dict["poke_img_frt"] = poke.image_front;
    dict["poke_img_bck"] = poke.image_back;
    POKE.push(dict)
  }
  return POKE
}

function showPokes(pokemons) {
  console.log(pokemons);
}

/*
Defines a function to render a list onto an HTML tbody element
*/
function renderList(item_list) {
  // sorts the film list array alphabetically by title
  item_list.sort((a, b) => (a.poke_id > b.poke_id ? 1 : -1));
  //creates a variable and stores the tbody element in the document body
  let tbody = document.querySelector(".list_gen tbody");
  //clears any existing content in the tbody element
  tbody.textContent = "";
  for (let i = 0; i < item_list.length; i++) {
    //renders a row on the table for each film
    let row = renderListRow(item_list[i]);
    row.addEventListener("click", function () {
      let capitalized_name = item_list[i].poke_name.charAt(0).toUpperCase() + item_list[i].poke_name.slice(1)
      poke_card_img.src=item_list[i].poke_img_frt
      poke_card_name.textContent = capitalized_name
      poke_card_number.textContent = "Number: " + item_list[i].poke_id
      poke_card_height.textContent = "Height: " + item_list[i].poke_height
      poke_card_weight.textContent = "Weight: " + item_list[i].poke_weight
    });
    //appends the new row to the table
    tbody.appendChild(row);
  }
}

/*
  Defines a function to render a row on the film table
  */
function renderListRow(list_item) {
  //creates the <tr> element for the row in a table
  let tr = document.createElement("tr");
  let name_poke = list_item.poke_name
  let capitalized_name = name_poke.charAt(0).toUpperCase() + name_poke.slice(1)

  //creates and appends the <td> elements
  tr.appendChild(renderListValue(list_item.poke_id));
  tr.appendChild(renderListValue(capitalized_name));
  tr.appendChild(renderListValue(list_item.poke_height));
  tr.appendChild(renderListValue(list_item.poke_weight));
  //returns the table row to the caller
  return tr;
}

/*
Defines a function to create new td elements and sets the appropriate ccs formatting
*/
function renderListValue(content, url) {
  //creates the new <td> element
  let td = document.createElement("td");

  //if it should be formatted as a non-numeric value
  if (url) {
    //if element is a URL, construct hyperlink
    let a = document.createElement("a");
    let linkText = document.createTextNode("Link");
    a.appendChild(linkText);
    a.title = "Link";
    a.target = "_blank";
    a.href = content;
    td.appendChild(a);
  } else {
    //If not url, sets its text content to the provided value
    td.textContent = content;
  }
  //returns the new element to the caller
  return td;
}

/*
  Defines a variable and stores the item filter element
  */
let searchInput = document.getElementById("item-filter");

/*
  Defines a function to filter the item list by matching user input to title
  */
function isItemFound(item) {
  //gets the user input and makes it lowercase
  let lowercaseUserInput = searchInput.value.toLowerCase();
  //gets the item title and makes it lowercase
  let lowercaseName = item.poke_name;
  //if the user input should match the iterated item title
  if (lowercaseName.indexOf(lowercaseUserInput) >= 0) {
    return true;
    //If the user input should not match the iterated item title
  } else {
    return false;
  }
}

/*
  Creates an event listener to call filter and render function on user input
  */
searchInput.addEventListener("input", function () {
  //creates a variable to store the filtered film array
  let filteredItems = POKE.filter(isItemFound);

  //updates the film table with the filtered film array
  renderList(filteredItems);
});
