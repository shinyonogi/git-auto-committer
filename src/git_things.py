import os
import logging

def git_configure(email, name):

    if os.system(f'git config user.email "{email}"') != 0:
        logging.error("Failed to execute 'git config email'.")
        return

    if os.system(f'git config user.name "{name}"') != 0:
        logging.error("Failed to execute 'git config name'.")
        return


def git_commit_and_push(commit_message):
    if os.system("git add .") != 0:
        logging.error("Failed to execute 'git add .'.")
        return

    if os.system(f'git commit -m "{commit_message}"') != 0:
        logging.error(f"Failed to execute 'git commit -m \"{commit_message}\"'.")
        return

    if os.system("git push") != 0:
        logging.error("Failed to execute 'git push'.")
