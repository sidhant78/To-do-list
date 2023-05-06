import PySimpleGUI

from function import readfile, writefile
import PySimpleGUI as ps
label = ps.Text("type in a todo")
input_ = ps.InputText(tooltip="what do you want to do", key="todo")
add_button = ps.Button('add')
listbox = ps.Listbox(values=readfile(), key="todos", enable_events=True, size=[45, 10])
add_button2 = ps.Button("edit")
add_button3 = ps.Button('Complete')
exit_button = ps.Button('Exit')
window = ps.Window('To-do app',
                   layout=[[label], [input_, add_button],
                           [listbox, add_button2,add_button3],
                           [exit_button]],
                   font=("Helvetica", 16))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "add":
            list1 = readfile()
            new_todo = value["todo"] + '\n'
            list1.append(new_todo)
            writefile(list1)
            window['todos'].update(values=list1)
            window['todo'].update(value="")
        case "edit":
            todo_to_edit = value['todos'][0]
            edited_todo = value['todo']
            list1 = readfile()
            z = list1.index(todo_to_edit)
            list1[z] = edited_todo
            writefile(list1)
            window['todos'].update(values=list1)
        case "todos":
            window["todo"].update(value['todos'][0])
        case "Complete":
            todo_to_delete = value['todos'][0]
            list1 = readfile()
            z1 = list1.index(todo_to_delete)
            list1.pop(z1)
            writefile(list1)
            window['todos'].update(values=list1)
            window['todo'].update(value="")
        case "Exit":
            break
        case ps.WIN_CLOSED:
            break
window.close()