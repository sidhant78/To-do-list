import function
import PySimpleGUI as ps
label = ps.Text("type in a todo")
input_ = ps.InputText(tooltip="what do you want to do")
add_button = ps.Button('Add')
window = ps.Window('To-do app', layout=[[label], [input_, add_button]])
window.read()
window.close()
