from subprocess import Popen, PIPE
from os import path
import re
repository  = 'E:\\Python\\\LearningPython'
gitpath = "C:\\Program Files\\Git\\cmd\\git.exe"
git_query = ""
git_status = ""


def gitadd ():
    git_command = [gitpath, 'add', '.']
    git_query = Popen(git_command, cwd=repository,  stdout=PIPE, stderr=PIPE)
    print("gitadd  git query" , git_query)
    (git_status, error) = git_query.communicate()
    print("git add output ", git_status)
    print("git add error  ",error)
    print("\n\n")
    if error:
        raise Exception("There is an error while git add \n")


def gitcommit (comment):
    git_command = [gitpath, 'commit', '-m', comment ]
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    print("git commit output \n", git_status)
    print("git commit error\n", error)
    if error:
        raise Exception("There is an error while comment \n")


def gitpush ():
    git_command = [gitpath, 'push']
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    (git_status, error) = git_query.communicate()
    print("git push output\n", git_status)
    print("git push error\n", error)


def gitstatus():
    git_command = [gitpath, 'status']
    git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
    # print(repository)
    (git_status, error) = git_query.communicate()
    # print("git git_status output \n", git_status)
    # print("git git_status error \n\n\n\n", error)
    return git_status


if __name__ == "__main__":

    git_status = gitstatus()
    # if git_query.poll() == 0:
    # print(git_status)
    checkuntrack = re.search("Untracked files", git_status.decode('utf-8'))
    print("checkuntrack \t", checkuntrack)
    if checkuntrack != None:
        try:
            gitadd()
            comment = input("Enter the comment to checking the code:")
            gitcommit(comment)
            gitpush()
        except:
            print("error in adding or commiting \n")
            pass

    else:
        print("No untracked files")
