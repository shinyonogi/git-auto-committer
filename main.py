import os
import random
from pathlib import Path
import openai

#This is my local file where the API key is stored
import key

#Importing the API Key from the local file
openai.api_key = key.api_key

#STORE: Answers in an array -> Same answers should not occur
answers = []

#DEFINE: Text that should be modified
text = "まゆこりんに勝ちたい。"


#DECLARING: a file name starting with 0x
file_name = '0x'
#This is how many times I commit
commit_times = random.randint(5, 15)

#FUNCTION: Takes a natural number n as an argument and returns the HEX
def convert_into_16(n):

    num_converted = 0

    if(n > 9):
        if(n == 10):
            num_converted = 'A'
        elif(n == 11):
            num_converted = 'B'
        elif(n == 12):
            num_converted = 'C'
        elif(n == 13):
            num_converted = 'D'
        elif(n == 14):
            num_converted = 'E'
        elif(n == 15):
            num_converted = 'F'
        else:
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
    if(c == 0):
        path_name = 'desktop/git-random-push/' + file_name
    else:
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

    content = f"""
    言われた分を違う表現に直して返してください。上限は一文です。
    ですが、以下の表現と完全に一致してはいけません。
    {str(answers)}
    """

    #DEFINE: The state
    context = [{"role": "system", "content": content}]

    #SEND: Message to OpenAI API
    send_message = context + [{"role": "user", "content": text}]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = send_message
    )

    #RECEIVE: Message from the server
    received_message = response.choices[0].message

    #APPEND: The answer to the list so it does not get repeated
    answers.append(received_message["content"])


    #DEFINE: the git commands as Strings
    git_add = 'git add .'
    git_commit = 'git commit -m "' + received_message["content"] + '"'

    #EXECUTES: git add . git commit -m "cat" git push
    os.system(git_add)
    os.system(git_commit)

    #RESET: the file name and path name so that it can be looped
    file_name = '0x'
    path_name = ''

git_push = 'git push'
os.system(git_push)
