let creatTodo = document.getElementById('create')
let todoField = document.getElementById('todo-field')
let doneField = document.getElementById('done-field')

let uncompleted = document.querySelectorAll('.uncompleted').length
let completed = document.querySelectorAll('.green').length


creatTodo.addEventListener('click', function(){
    let text = document.getElementById('todo-text').value
    let title = document.getElementById('todo-title').value
    console.log(text)
    makeCard(title, text)
})

function updateRatio(){
    uncompleted = document.querySelectorAll('.uncompleted').length
    completed = document.querySelectorAll('.green').length

    chart.data = [{
        'title': 'uncompleted',
        'count': uncompleted
    }, {
        'title': 'completed',
        'count': completed 
    }]
    
}

function makeCard(title='Uncompleted item', body='no-text'){
    

    const layerOne = document.createElement('div')
    layerOne.classList.add('col')
    layerOne.classList.add('s4')
    layerOne.classList.add('m4')
    layerOne.classList.add('uncompleted')

    const layerTwo = document.createElement('div')
    layerTwo.classList.add('card')
    layerTwo.classList.add('blue-grey')
    layerTwo.classList.add('darken-1')

    const layerThree = document.createElement('div')
    layerThree.classList.add('card-content')
    layerThree.classList.add('white-text')
    
    const layerTitle = document.createElement('span')
    layerTitle.classList.add('card-title')
    layerTitle.textContent = `${title}`

    const layerBody = document.createElement('p')
    layerBody.textContent = `${body}`

    const layerAction = document.createElement('div')
    layerAction.classList.add('card-action')
    
    const layerComplete = document.createElement('a')
    layerComplete.textContent = 'Mark Completed'
    layerComplete.addEventListener('click', function(){
        todoField.removeChild(layerOne)
        doneField.append(layerOne)
        layerThree.classList.remove('blue-grey')
        layerOne.classList.remove('uncompleted')
        layerThree.classList.add('green')
        layerAction.removeChild(layerComplete)
        updateRatio()

    })


    const layerDelete = document.createElement('a')
    layerDelete.textContent = 'Delete'
    layerDelete.addEventListener('click', function(){
        layerDelete.parentNode.parentNode.parentNode.parentNode.removeChild(layerDelete.parentNode.parentNode.parentNode)
        updateRatio()

    })

    layerOne.append(layerTwo)
    layerTwo.append(layerThree)
    layerTwo.append(layerThree)
    layerThree.append(layerTitle)
    layerThree.append(layerBody)
    
    layerTwo.append(layerAction)
    layerAction.append(layerComplete)
    layerAction.append(layerDelete)

    todoField.append(layerOne)
    updateRatio()


    // Core concept here is I made materlize cards on each click. using the materliaze css example to layer it out. 
    // https://materializecss.com/cards.html

    // God I hate layers
        // ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        // ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
        // ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
        // ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
        // ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
        // ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        // ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉


}

// chart crap

var chart = am4core.create("chartdiv", am4charts.PieChart);

chart.data = [{
    'title': 'uncompleted',
    'count': uncompleted
}, {
    'title': 'completed',
    'count': completed 
}]

var pieSeries = chart.series.push(new am4charts.PieSeries());

pieSeries.dataFields.value = "count";
pieSeries.dataFields.category = "title";