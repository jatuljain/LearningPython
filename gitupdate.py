from subprocess import Popen, PIPE
from os import path
import re
repository  = 'E:\\Python\\git_projects'
gitpath = "C:\\Program Files\\Git\\cmd\\git.exe"

def gitadd ():
    git_command = [gitpath, 'add', '.']
    git_query = Popen(git_command, cwd=repository,  stdout=PIPE, stderr=PIPE)
    print("gitadd  git query" , git_query)
    (git_status, error) = git_query.communicate()
    print("git add output \n\n ",git_status)
    print("git add error \n\n ",error)
    return error

def gitcommit (comment):
    git_command = [gitpath, 'commit',  '-m', comment ]
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    print("git commit output", git_status)
    print("git commit error", error)

def gitpush ():
    git_command = [gitpath, 'commit', 'push']
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    print("git push output", git_status)
    print("git push error", error)



git_command = [gitpath, 'status']
git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
print(repository)
(git_status, error) = git_query.communicate()
print("git git_status output \n", git_status)
print("git git_status error \n", error)

if git_query.poll() == 0:

    # print(git_status)
    checkuntrack = re.search("Untracked files", git_status.decode('utf-8'))
    print("checkuntrack \t", checkuntrack)
    if checkuntrack != None:
        try:
            gitadd()
            comment = input("Enter the comment to checking the code:")
            gitcommit(comment)
            gitpush()
        except ValueError:
            print("error in adding or commiting \n")
            pass

    else:
        print("No untracked files")
