todo_list = []

def create_todo(todo_str):
    id = len(todo_list)
    todo_list.append([id, todo_str])
    
def read_todo():
    for todo in todo_list:
        print(str(todo[0]) + " - " + str(todo[1]))

def update_todo(id, update_str):
    for todo in todo_list:
        if todo[0] == id:
            todo[1] = update_str
            break

def delete_todo(id):
    copy_todo_list = todo_list.copy()
    for todo in copy_todo_list:
        if todo[0] == id:
            index = copy_todo_list.index(todo)
            todo_list.pop(index)
            break

read_todo()
create_todo("Do the dishes")
create_todo("Walk the dog")
create_todo("Brush your teeth")
read_todo()
print("")
update_todo(1, "Buy a dog")
read_todo()
print("")
delete_todo(2)
read_todo()
print("")
            