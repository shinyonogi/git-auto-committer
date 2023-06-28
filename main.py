import os
import random
from pathlib import Path

#DECLARING: a file name starting with 0x
file_name = '0x'
#This is how many times I commit
commit_times = random.randint(5, 15)

#FUNCTION: Takes a natural number n as an argument and returns the HEX
def convert_into_16(n):

    num_converted = 0

    if(n > 9):
        match n:
            case 10:
                num_converted = 'A'
            case 11:
                num_converted = 'B'
            case 12:
                num_converted = 'C'
            case 13:
                num_converted = 'D'
            case 14:
                num_converted = 'E'
            case 15:
                num_converted = 'F'
            case _:
                num_converted = 'error occured'
    else:
        num_converted = n

    return num_converted

#LOOP: As many times as I should commit on a day
for c in range(commit_times):
    #CREATING: Randomly generates a 5bit file name
    for i in range(10):
        file_name += str(convert_into_16(random.randint(0, 15)))

    #ATTENTION: Path name is going to be different after you change the directory below
    match c:
        case 0:
            path_name = 'desktop/git-random-push/' + file_name
        case _:
            path_name = file_name

    #CREATING: Touch a file with the created file name
    Path(path_name).touch()

    #Writes the sentence into the file
    f = open(path_name, "a")
    f.write("I'm smiling :)")
    f.close()

    #Changing directory (CD)
    #ATTENTION: Since you commit multiply times -> Changing the directory multiple times does not work
    try:
        cd = 'desktop/git-random-push/'
        os.chdir(cd)
        #os.system('pwd')
    except FileNotFoundError:
        pass

    #DEFINE: the git commands as Strings
    git_add = 'git add .'
    git_commit = 'git commit -m "cat"'
    git_push = 'git push'

    #EXECUTES: git add . git commit -m "cat" git push
    os.system(git_add)
    os.system(git_commit)
    os.system(git_push)

    #RESET: the file name and path name so that it can be looped
    file_name = '0x'
    path_name = ''

