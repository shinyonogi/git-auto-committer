import os
import random
from pathlib import Path

#DECLARING: a file name starting with 0x
file_name = '0x'

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

#This is how many times I commit
commit_times = random.randint(5, 15)

for c in range(commit_times):
    #CREATING: Randomly generates a 5bit file name
    for i in range(10):
        file_name += str(convert_into_16(random.randint(0, 15)))

    match c:
        case 0:
            #CREATING: Touch a file with the created file name
            path_name = 'desktop/git-random-push/' + file_name
        case _:
            path_name = file_name

    Path(path_name).touch()

    #Writes the sentence into the file
    f = open(path_name, "a")
    f.write("I'm smiling :)")
    f.close()

    #Changing directory (CD)
    cd = 'desktop/git-random-push/'
    os.chdir(cd)
    #os.system('pwd')

    #Executes git add . git commit -m "cat" git push
    git_add = 'git add .'
    git_commit = 'git commit -m "cat"'
    git_push = 'git push'

    os.system(git_add)
    os.system(git_commit)
    os.system(git_push)

    #Reset the file name and path name so that it can be looped
    file_name = '0x'
    path_name = ''

