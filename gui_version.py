import PySimpleGUI

from function import readfile, writefile
import PySimpleGUI as ps
label = ps.Text("type in a todo")
input_ = ps.InputText(tooltip="what do you want to do", key="todo")
add_button = ps.Button('add')
listbox = ps.Listbox(values=readfile(), key="todos",enable_events=True,size=[45, 10])
window = ps.Window('To-do app',
                   layout=[[label], [input_, add_button]],
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
        case ps.WIN_CLOSED:
            break

window.close()