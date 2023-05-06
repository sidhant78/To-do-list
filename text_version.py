from function import readfile, writefile
import time
print("today is",time.strftime("%d-%m-%y,%H-%M-%S"))
while True:
    text = input('type add ,show,edit,completed or exit')
    text = text.strip()
    if text.startswith("add"):
        todo = text[4:] +'\n'
        list = readfile("guii.txt")
        list.append(todo)
        writefile(list,"guii.txt")
    elif text.startswith("show"):
        list = readfile("guii.txt")
        new_list = [l.strip('\n') for l in list]
        for index,l in enumerate(new_list):
            print(f'{index+1}-{l.capitalize()}')
        if len(list) > 7:
            print("seems like a busy day")
        else:
            print("you can manage it with ease")
    elif text.startswith("edit"):
        try:
            to_replace = int(text[5:])
            list = readfile("guii.txt")
            list[to_replace-1]=input('write the new task') + "\n"
            writefile(list,"guii.txt")
        except ValueError:
            print('your command is invalid')
            continue
    elif text.startswith("completed"):
        try:
            completed = int(text[10:])
            list = readfile("guii.txt")
            todo_to_remove = list[completed-1]
            list.pop(completed-1).strip('\n')
            writefile(list,"guii.txt")
            print(f'the removed task is {todo_to_remove}')
        except IndexError:
            print('type the correct index')
            continue
    elif text.startswith("exit"):
        break
print('see you soon')
