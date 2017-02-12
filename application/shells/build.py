import fileinput

class ShellBuild:

    shell_type = ''

    def __init__(self, filename, shell_type, function):
        print("Shell Type is: " + shell_type)
        if shell_type == 'php':
            try:
                shellCont = None
                f = open('shells/php_shell.php', 'r')
                shellCont = f.read()
                f.close()

                finalCont = shellCont.replace('cmd', function)
                fileCont = open(filename, 'w')
                fileCont.write(finalCont)
                fileCont.close()
            except:
                print("Cannot build shell")
                print(f)
        else:
            print("We only support php")
