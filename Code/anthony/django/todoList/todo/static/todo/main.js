
const tableBody = document.getElementById('table-body');
const editForm = document.getElementById('edit-form');

editForm.style.display = 'none';


for(row of tableBody.children) {
  row.addEventListener('click', createForm);
};

function createForm(){
  console.log(this.children[0]);
  editForm.style.display = 'block';
  editForm.children[1].value = this.children[0].innerText
  editForm.children[2].value = this.id
  // editForm.children[3].checked = this.children[3].value == 'None' ? false : true

  if (this.children[3].innerText === 'None'){
    editForm.children[3].children[0].checked = false
  } else {
    editForm.children[3].children[0].checked = true
  }
}