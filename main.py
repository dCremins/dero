import time
from commands import exit_commands
from database import DatabaseCommands

def main():
    # Start an infinite loop to keep the chatbot running.
    while True:
        # Ask the user to enter a message or 'exit' to leave.
        message = boot()
        
        # Check if the message is 'exit', to end the loop and shut down the chatbot.
        if message == False or message.lower() in exit_commands:
            break  # Breaks the loop, ending the function and closing the chatbot.

def boot():
    loadingBar(prefix = 'Booting System...', length = 20)
    DatabaseCommands.create_users_table()
    print("""
          _____                    _____                    _____                   _______         
         /\    \                  /\    \                  /\    \                 /::\    \        
        /::\    \                /::\    \                /::\    \               /::::\    \       
       /::::\    \              /::::\    \              /::::\    \             /::::::\    \      
      /::::::\    \            /::::::\    \            /::::::\    \           /::::::::\    \     
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \    
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \   
   /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \  
  /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\ 
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |
/:::/____/     \:::|    |/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    ||:::|____|     |:::|    |
\:::\    \     /:::|____|\:::\   \:::\   \::/    /\::/   |::::\  /:::|____| \:::\    \   /:::/    / 
 \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /   \:::\    \ /:::/    /  
  \:::\    \ /:::/    /    \:::\   \:::\    \            |:::::::::/    /     \:::\    /:::/    /   
   \:::\    /:::/    /      \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /    
    \:::\  /:::/    /        \:::\   \::/    /           |::| \::/____/         \::::::::/    /     
     \:::\/:::/    /          \:::\   \/____/            |::|  ~|                \::::::/    /      
      \::::::/    /            \:::\    \                |::|   |                 \::::/    /       
       \::::/    /              \:::\____\               \::|   |                  \::/____/        
        \::/____/                \::/    /                \:|   |                   ~~              
         ~~                       \/____/                  \|___|                                   

-----------------------------------------------------------------------------------------------------
          
        D.E.R.O. is a virtual assistant program created by Devin Cremins
        Copyright (c) 2024       

-----------------------------------------------------------------------------------------------------
                                                            
    """)
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
            return await_command()
        else:
            print("LOGIN FAILED")
            return menu()
    elif message.lower() in ["2", "create", "create user", "user"]:
        return create_user()
    elif message.lower() in ["3", "exit"]:
        return "exit"
    else:
        print("UNKNOWN COMMAND")
        return menu()

def create_user():
    user = input("> USERNAME: ")
    password = input("> PASSWORD: ")
    name = input("> NAME: ")
    loadingBar(prefix = 'Checking Input:', length = 5)
    DatabaseCommands.create_user(user, password, name)
    return menu()

def login():
    user = input("> USERNAME: ")
    password = input("> PASSWORD: ")
    loadingBar(prefix = 'Checking Input:', length = 20)
    return DatabaseCommands.validate_user(user, password)

def await_command():
    message = input("> ")
    loadingBar(prefix = 'Checking Input:', length = 20)
    return determine_input(message)

def loadingBar (prefix = '', length = 100 ):
    for i in range(length + 1):
        bar = '|' * i + '-' * (length - i)
        print(f'\r{prefix} |{bar}| ', end = "\r")
        time.sleep(0.1)
    print()

def determine_input(message):
    if (message in ["test"]):
        return
    else:
        return message

def handle_query():
    return

def handle_reminder():
    return

def handle_command():
    return

if __name__ == "__main__":
    main()