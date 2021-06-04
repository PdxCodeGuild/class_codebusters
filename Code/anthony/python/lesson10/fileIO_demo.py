
"""
with open('./sample.txt', 'r') as file:
    contents = file.read()


print(contents)
"""

# Read a file of todos
with open('./todos.txt') as file:
    contents = file.read()

# Show current todos to user
contents = contents.split('\n')
if contents[-1] == "":
    contents.pop()
print(contents)

while True:
    # Let the user add more todos
    todo = input("Enter task: ")
    if todo == 'done':
        break
    contents.append(todo)

# Save any added todos to the file
# contents = "\n".join(contents)
with open('./todos.txt', 'w') as file:
    file.write(contents)
