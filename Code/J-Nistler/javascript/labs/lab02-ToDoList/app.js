//JS code for the list generation and rendering

/*
Defines a function to render a list onto an HTML tbody element
*/
function renderList(item_list01, item_list02) {
  //creates a variable and stores the tbody element in the document body
  let tbody = document.querySelector(".list_gen tbody");
  //clears any existing content in the tbody element
  tbody.textContent = "";
  //generates the TODO list
  for (let i = 0; i < item_list01.length; i++) {
    let row = renderListRow(item_list01[i]);
    row.id = "item" + i;
    //appends the new row to the table
    tbody.appendChild(row);
  }
  //generates the COMPLETED List
  for (let i = 0; i < item_list02.length; i++) {
    let row = renderListRow(item_list02[i], i + 1);
    row.className = "strikeout";
    //appends the new row to the table
    tbody.appendChild(row);
  }
}

/*
  Defines a function to render a row on the list table
  */
function renderListRow(list_item, num) {
  //creates the <tr> element for the row in a table
  let tr = document.createElement("tr");

  //creates and appends the <td> elements
  tr.appendChild(renderCheck(list_item, num));
  tr.appendChild(renderListValue(list_item));
  tr.appendChild(renderDelete(list_item));
  //returns the table row to the caller
  return tr;
}

/*
Defines a function to create new td elements and sets the appropriate ccs formatting
*/
function renderListValue(content) {
  //creates the new <td> element
  let td = document.createElement("td");
  //If not url, sets its text content to the provided value
    td.textContent = content;
  //returns the new element to the caller
  return td;
}

function renderCheck(content, num) {
  let td = document.createElement("td");
  let check = document.createElement("input");
  check.type = "checkbox";
  check.className = "todo-check";
  if (num) {
    check.checked = true;
  }
  td.appendChild(check);
  td.addEventListener("click", function () {
    if (DONE.includes(content)) {
      DONE.splice(DONE.indexOf(content), 1);
      TODO.push(content);
    } else {
      TODO.splice(TODO.indexOf(content), 1);
      DONE.push(content);
    }
    renderList(TODO, DONE);
  });
  return td;
}

function renderDelete(content) {
  let td = document.createElement("td");
  let spn = document.createElement("span");
  let labelText = document.createTextNode("Delete");
  spn.appendChild(labelText);
  spn.className = "badge rounded-pill bg-danger";
  spn.addEventListener("click", function () {
    if (DONE.includes(content)) {
      DONE.splice(DONE.indexOf(content), 1);
    } else {
      TODO.splice(TODO.indexOf(content), 1);
    }
    renderList(TODO, DONE);
    for (var i = 0; i < allDeleteButtons.length; i++) {
      allDeleteButtons[i].style.visibility = "visible";
    }
  });
  td.appendChild(spn);
  return td;
}

renderList(TODO, DONE);

/*
Allow user to add element to the ToDo
*/
const submitButton = document.getElementById("button-submit");
const deleteButton = document.getElementById("button-delete");
const allDeleteButtons = document.getElementsByClassName(
  "badge rounded-pill bg-danger"
);
const checkboxes = document.getElementsByClassName("todo-check");

submitButton.addEventListener("click", function () {
  let newTodo = document.getElementById("todo-text").value;
  if (newTodo && TODO.includes(newTodo) == false) {
    TODO.push(newTodo);
    renderList(TODO, DONE);
  }
  document.getElementById("todo-text").value = "";
});

deleteButton.addEventListener("click", function () {
  if ((allDeleteButtons[0].style.visibility == "visible")) {
    for (var i = 0; i < allDeleteButtons.length; i++) {
      allDeleteButtons[i].style.visibility = "hidden";
    }
  } else {
    for (var i = 0; i < allDeleteButtons.length; i++) {
      allDeleteButtons[i].style.visibility = "visible";
    }
  }
});
