
from commands import copyright, loadingBar
from parsing import await_command, handle_unknown
from database import DatabaseCommands

def boot():
    loadingBar(prefix = 'Booting System...', length = 20)
    DatabaseCommands.create_users_table()
    print(copyright)
    menu()

def menu():
    message = input("""
    PLEASE IDENTIFY
                    
        [1] LOGIN
        [2] CREATE USER
        [3] EXIT              
     > """)
    if message.lower() in ["1", "login"]:
        success = login()
        if success:
            print("WELCOME %s" % success)
            return await_command()
        else:
            print("LOGIN FAILED")
            return menu()
    elif message.lower() in ["2", "create", "create user", "user"]:
        return create_user()
    elif message.lower() in ["3", "exit"]:
        return "exit"
    else:
        handle_unknown()
        return menu()

def create_user():
    user = input("> USERNAME: ")
    password = input("> PASSWORD: ")
    name = input("> NAME: ")
    loadingBar(prefix = 'Checking Input:', length = 5)
    DatabaseCommands.create_user(user, password, name)
    return menu()

def login() -> str:
    user = input("> USERNAME: ")
    password = input("> PASSWORD: ")
    loadingBar(prefix = 'Checking Input:', length = 20)
    return DatabaseCommands.validate_user(user, password)
