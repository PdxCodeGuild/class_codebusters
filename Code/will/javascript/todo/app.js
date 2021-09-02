const newTodo = document.getElementById('newtodo')
const addTodo = document.getElementById('addbutton')
const incomplete = document.getElementById('incomplete')
const complete= document.getElementById('complete')


const todoItems = []
const completeItems = []

function displayIncomplete(){
  for(let item of todoItems){
    const divItem = document.createElement('div')
    divItem.setAttribute('class', 'item')
    const p = document.createElement('p')
    p.textContent = item
    const div = document.createElement('div')
    const btnComplete = document.createElement('button')
    btnComplete.textContent = 'Mark Complete'
    btnComplete.addEventListener('click', function() {
      completeTodo(btnComplete, todoItems, completeItems)
    })
   
    divItem.append(p)
    divItem.append(div)
    div.append(btnComplete)

    incomplete.append(divItem)
  }
}

function displayCompleted(){
  for(let item of completeItems){
    const divItem = document.createElement('div')
    divItem.setAttribute('class', 'item')
    const p = document.createElement('p')
    p.textContent = item
    const div = document.createElement('div')



    divItem.append(p)
    divItem.append(div)
    complete.append(divItem)
  }
}

function clearList(list){
  while(list.firstChild){
    list.removeChild(list.firstChild)
  }
}

function completeTodo(btn, arrayFrom, arrayTo){
  const item = btn.parentElement.parentElement
  const index = arrayFrom.indexOf(item.firstChild.textContent)
  const [complete] = arrayFrom.splice(index, 1)
  arrayTo.push(complete)

  clearList(incomplete)
  clearList(complete)
  displayIncomplete()
  displayCompleted()
}


addTodo.addEventListener('click', function () {
  todoItems.push(newTodo.value)
  newTodo.value = ''
  clearList(incomplete)
  displayIncomplete()
})