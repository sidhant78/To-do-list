def readfile(parameter='mem.txt'):
    """ reads an already existing file and readlines command assigns a list to a variable list local"""
    with open(parameter, 'r') as file_local:
        list_local = file_local.readlines()
        return list_local


def writefile(list_arg,parameter='mem.txt'):
    """uses a text file to edit info"""
    with open(parameter,'w') as file_local2:
        file_local2.writelines(list_arg)
