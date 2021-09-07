

    let add_bt = document.querySelector('#add_bt');
    let todo_input = document.querySelector('#todo_input');
    let list = document.querySelector('#todo_list');
    let completed_list = document.querySelector('#completed_list');



    add_bt.onclick = function() {
        let text = todo_input.value;
        if (text === '') {
            return;
        }
        todo_input.value = '';
        let li = document.createElement('li');
        li.classList.add('todo_item');
        let text_div = document.createElement('div');
        text_div.innerHTML = text;

        let button_complete = document.createElement('button');
        button_complete.innerHTML = '&#x2713;';
        button_complete.onclick = function() {
            list.removeChild(this.parentElement);
            let li = document.createElement('li');
            li.innerText = text;
            completed_list.appendChild(li);
        };

        let button_remove = document.createElement('button');
        button_remove.innerHTML = '&#x2715;';
        button_remove.onclick = function() {
            list.removeChild(this.parentElement);
        };




        li.appendChild(text_div);
        li.appendChild(button_complete);
        li.appendChild(button_remove);
        list.appendChild(li);
    }

