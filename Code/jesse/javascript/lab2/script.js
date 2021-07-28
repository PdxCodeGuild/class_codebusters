const newTodo = document.getElementById('new-todo')
const addTodo = document.getElementById('add-todo')
const listItems = document.getElementById('list-items')
const listComplete = document.getElementById('list-complete')

const todoItems = []
const completeItems = []

// Generate todo items with 'complete' and 'remove' buttons 
function displayTodoItems() {

   

    // remove all previously displayed todo items
    while (listItems.firstChild) {
        listItems.removeChild(listItems.firstChild)
    }

    // generate todo items from 'todoItems' array with html elements, and attach to document
    for (item of todoItems) {
        // make 'complete' button for item
        const btnComplete = document.createElement('button')
        btnComplete.textContent = '✅'

        // change item to a completed status when its 'complete' button is clicked
        btnComplete.addEventListener('click', () => {

            // move completed item's text from 'todoItems' array to 'completeItems' array
            const index = todoItems.indexOf(btnComplete.parentElement.lastChild.textContent)
            const complete = todoItems.splice(index, 1)
            completeItems.push(complete)

            // remove item from document
            listItems.removeChild(btnComplete.parentElement)
            
            // remove all previously displayed completed items from document
            while (listComplete.querySelector('.complete-item')) {
                listComplete.removeChild(listComplete.querySelector('.complete-item'))
            }

            // generate completed todo items from 'completeItems' array, attach to document
            for (item of completeItems) {
                const completeDiv = document.createElement('div')
                completeDiv.setAttribute('class', 'complete-item')
                completeDiv.textContent = item
                listComplete.appendChild(completeDiv)
            }
        })

        // make 'remove' button for item
        const btnRemove = document.createElement('button')
        btnRemove.textContent = '❎'

        // remove item when its 'remove' button is clicked
        btnRemove.addEventListener('click', () => {
            // remove removed item's text from 'todoItems' array
            const index = todoItems.indexOf(btnRemove.parentElement.lastChild.textContent)
            todoItems.splice(index, 1)

            // remove item from document
            listItems.removeChild(btnRemove.parentElement)
        })

        // create parent 'div' for item
        const div = document.createElement('div')
        div.setAttribute('class', 'todo-item')

        // make p tag with text for item
        const p = document.createElement('p')
        p.textContent = item
          
        // append text and buttons of item to 'li' parent, append to document
        
        div.appendChild(btnComplete)
        div.appendChild(btnRemove)
        div.appendChild(p)
        listItems.appendChild(div)
    }

    
}

// make item based on data entered in input field of document
// add item to 'todoItems' array, clear input field, and call function
addTodo.addEventListener('click', () => {
    todoItems.push(newTodo.value)
    newTodo.value = ''
    displayTodoItems()
})



