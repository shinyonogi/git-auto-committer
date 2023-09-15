import os

def git_commit_and_push(commit_message):
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")
