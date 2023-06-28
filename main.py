import os
import random
from pathlib import Path

file_name = '0x'

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

for i in range(10):
    file_name += str(convert_into_16(random.randint(0, 15)))

Path('desktop/git-random-push/' + file_name).touch()



