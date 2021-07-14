# Todo

## Part 1

Let's create a simple todo app. This can be done creating a model for representing a `TodoItem`. The index page should have a list of all the todo items (showing only the name). There should also be a text field and a button (in a form), When the user clicks the button it should save a new todo item to the database and show the newly-added item in the list. Use one view to render the template, and another view to receive the form submission and redirect back to the first view.


### Steps

1. Create the project and app
2. Create the index view and route to get there, test it to make sure you can complete a request-response cycle
3. Create your models, run migrations, log into your admin panel and enter some information (test CRUD)
4. Go back to your index view, get data out of the database and render it in a template
5. Create the form in your template, create a save_todo_item view, make sure your form data is received by the view (`print(request.POST)`)
6. Using the form data, create an instance of your TodoItem model, save it, and redirect back to the index page


### Model

- TodoItem
  - text - CharField
  - created_date - DateTimeField(auto_now_add=True)
    - auto_now_add=True will automatically add the date when the TodoItem is created.


### Views

- Index Page
  - List of the uncompleted todo items including text, and created date
- Save Todo Item
  - Receive the form submission and create a new todo item, then redirect back to the first view


## Part 2 (optional)

Add a BooleanField `completed` to the `TodoItem` model.

Show the completed items separately (at the bottom of the table or in another table), with grey text color and a line through them (`text-decoration:line-through`).

Add a `complete` button next to each todo item, these can be `a` tags which link to another view that receives the `id` of the todo item in the path, sets the completed date, and redirects back to the first view.

Add a `delete` button next to each todo item, which can also be an `a` tag that links to another view which deletes the item and redirects back to the first view.

### Model

- TodoItem
  - text - CharField
  - created_date - DateTimeField(auto_now_add=True)
    - auto_now_add=True will automatically add the date when the TodoItem is created.
  - completed - BooleanField

### Views

- Index Page
  - List of the uncompleted todo items including text, and created date
- Save Todo Item
  - Receive the form submission and create a new todo item, then redirect back to the first view
- Complete Todo Item
  - Toggle complete property on the TodoItem True/False
- Delete Todo Item
  - Remove TodoItem from the database
```python
  todo = TodoItem.objects.get(id=todo_id)
  todo.delete()
```

