//JS code for the list generation and rendering

/*
Defines a function to render a list onto an HTML tbody element
*/
function renderList(item_list) {
    // sorts the film list array alphabetically by title
    item_list.sort((a, b) => (a.title > b.title ? 1 : -1));
    //creates a variable and stores the tbody element in the document body
    var tbody = document.querySelector(".list_gen tbody");
    //clears any existing content in the tbody element
    tbody.textContent = "";
     //renders a row on the table for each film
    var row = renderListRow(item_list[i]);
    //appends the new row to the table
    tbody.appendChild(row);
  }
  
  /*
  Defines a function to render a row on the film table
  */
  function renderListRow(list_item) {
    //creates the <tr> element for the row in a table
    var tr = document.createElement("tr");
  
    //creates and appends the <td> elements
    tr.appendChild(renderListValue(list_item.number));
    tr.appendChild(renderListValue(list_item.name));
    tr.appendChild(renderListValue(list_item.types));
    tr.appendChild(renderListValue(list_item.image_front, true));
    tr.appendChild(renderListValue(list_item.image_back, true));
    //returns the table row to the caller
    return tr;
  }
  
/*
Defines a function to create new td elements and sets the appropriate ccs formatting
*/
function renderListValue(content, url) {
    //creates the new <td> element
    var td = document.createElement("td");
  
    //if it should be formatted as a non-numeric value
    if (url) {
      //if element is a URL, construct hyperlink
      var a = document.createElement("a");
      var linkText = document.createTextNode("Link");
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
  var searchInput = document.getElementById("item-filter");
  
  /*
  Defines a function to filter the item list by matching user input to title
  */
  function isItemFound(item) {
    //gets the user input and makes it lowercase
    var lowercaseUserInput = searchInput.value.toLowerCase();
    //gets the item title and makes it lowercase
    var lowercaseTitle = item.title.toLowerCase();
    //if the user input should match the iterated item title
    if (lowercaseTitle.indexOf(lowercaseUserInput) >= 0) {
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
    var filteredItems = list.filter(isItemFound);
  
    //updates the film table with the filtered film array
    renderList(filteredItems);
  });