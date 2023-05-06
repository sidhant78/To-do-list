FILEPATH = "mem.txt"


def readfile(parameter=FILEPATH):
    """ reads an already existing file and readline command assigns a list to a variable list local"""
    with open(parameter, 'r') as file_local:
        list_local = file_local.readlines()
        return list_local


def writefile(list_arg, parameter=FILEPATH):
    """uses a text file to edit info"""
    with open(parameter, 'w') as file_local2:
        file_local2.writelines(list_arg)
