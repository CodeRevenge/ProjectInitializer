from os import system, name, path, getcwd, mkdir, removedirs, rename, chdir
import requests
import git
import virtualenv
from subprocess import check_call


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def yes_no_option(option=""):
    if option == "yes" or option == "y" or option == "Y":
        return True
    elif option == "no" or option == "n" or option == "N":
        return False
    else:
        raise Exception("Not valid option")


def create_python_project():
    clear()
    print("Creating Python Project")
    name = input(f"Project name: ")
    git_enable = yes_no_option(input(f"Using Git?(Y/N): "))
    docker = yes_no_option(input(f"Using Docker?(Y/N): "))
    venv = yes_no_option(input(f"Using Virtual env?(Y/N): "))

    if venv:
        venv_name = input("Virtual env name: ")

    final = f"Project name: {name} \n"
    if git_enable:
        final += "Using GIT\n"
    if docker:
        final += "Using Docker\n"
    if venv:
        final += f"Using Virtual Enviroment ({venv_name})"

    clear()
    print(final)
    create = yes_no_option(input("Create project?(Y/N): "))

    if create:
        if not path.isdir(f"./{name}"):
            try:
                mkdir(f"./{name}")
                mkdir(f"./{name}/src")
                print(f"-\t/{name} and /{name}/src dir created!")

                app = open(f"{name}/src/app.py", "w+")
                app.write("if __name__ == '__main__': \n\tpass")
                app.close()

                print("-\tapp.py file created!")

            except OSError:
                raise Exception(
                    f"ERROR: Creation of the directory {name} failed")
                print()
        else:
            raise Exception(f"ERROR: {name} dir already exist!")

        if git:
            git.Repo.init(name)
            print(f"-\t{name} repo created!")

            git_ignore = open(f"{name}/.gitignore", "w+")
            link = "https://www.toptal.com/developers/gitignore/api/python,visualstudiocode,pycharm,git,virtualenv,pydev"

            response = requests.get(link)

            if response.status_code == 200:
                git_ignore_set = response.text
                git_ignore.write(git_ignore_set)
                print("-\t.gitignore created!")
                git_ignore.close()
            else:
                removedirs(f"./{name}")
                raise Exception(
                    "ERROR: .gitignore content has not been placed due to bad request to gigignore.io")

            readme = open(f"{name}/README.md", "w+")
            readme.write(f"# {name}")
            readme.close()

            print("-\tREADME.md has been created!")

        if docker:
            docker_file = open(f"{name}/Dockerfile", "w+")
            docker_file.write("FROM python:latest")
            docker_file.close()
            print("-\tDockerfile created!")

            docker_ignore = open(f"{name}/.dockerignore", "w+")
            if venv:
                docker_ignore.write(f"{venv_name}")
            docker_ignore.close()
            print("-\t.dockerignore created!")

        if venv:
            virtualenv.cli_run([f"{name}/.{venv_name}"])
            print(f"-\tVirtual environment {venv_name} created!")


def create_nodejs_project():
    clear()
    print("Creating NodeJS Project")
    name = input(f"Project name: ")
    while True:
        try:
            initializer = int(input("Use [1] Yarn or [2] NPM ?: "))
            if initializer < 1 or initializer > 2:
                raise Exception()
            break
        except:
            print("Not a valid option!")
    git_enable = yes_no_option(input(f"Using Git?(Y/N): "))
    docker = yes_no_option(input(f"Using Docker?(Y/N): "))

    final = f"Project name: {name} \n"
    final += "Using Yarn\n" if initializer == 1 else "Using NPM\n"
    if git_enable:
        final += "Using GIT\n"
    if docker:
        final += "Using Docker\n"

    clear()
    print(final)
    create = yes_no_option(input("Create project?(Y/N): "))

    if create:
        if not path.isdir(f"./{name}"):
            try:
                mkdir(f"./{name}")
                mkdir(f"./{name}/src")
                print(f"-\t/{name} and /{name}/src dir created!")

                app = open(f"{name}/index.js", "w+")
                app.write('console.log("Hello Wordl!")')
                app.close()

                print("-\tapp.js file created!")

            except OSError:
                raise Exception(
                    f"ERROR: Creation of the directory {name} failed")
                print()
        else:
            raise Exception(f"ERROR: {name} dir already exist!")

        if git:
            git.Repo.init(name)
            print(f"-\t{name} repo created!")

            git_ignore = open(f"{name}/.gitignore", "w+")
            link = "https://www.toptal.com/developers/gitignore/api/yarn,visualstudiocode,node,webstorm,mean"

            response = requests.get(link)

            if response.status_code == 200:
                git_ignore_set = response.text
                git_ignore.write(git_ignore_set)
                print("-\t.gitignore created!")
                git_ignore.close()
            else:
                removedirs(f"./{name}")
                raise Exception(
                    "ERROR: .gitignore content has not been placed due to bad request to gigignore.io")

            readme = open(f"{name}/README.md", "w+")
            readme.write(f"# {name}")
            readme.close()

            print("-\tREADME.md has been created!")

        if docker:
            docker_file = open(f"{name}/Dockerfile", "w+")
            docker_file.write("FROM python:latest")
            docker_file.close()
            print("-\tDockerfile created!")

            docker_ignore = open(f"{name}/.dockerignore", "w+")
            docker_ignore.close()
            print("-\t.dockerignore created!")

        chdir(f"{getcwd()}/{name}")
        if initializer == 1:

            check_call("yarn init", shell=True)
        elif initializer == 2:
            check_call("npm init", shell=True)
        print("-\tpackage.json created!")


def error():
    print("Not a valid option")


if __name__ == "__main__":
    project_types = {
        -1: error,
        0: create_python_project,
        1: create_nodejs_project
    }

    selection_options = f'''
        Projects Creator by CodeKiller (CodeRevenge)
        Select one option
        [0] Python
        [1] NodeJS

    Option:
    '''

    clear()
    try:
        project_type = int(input(selection_options))
        project_types.get(project_type, error)()
    except Exception as e:
        print(str(e))
    except:
        print("Invalid option")
