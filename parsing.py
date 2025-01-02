from commands import loadingBar, exit_commands, query_commands, help_commands

def await_command():
    print("AWAITING USER COMMAND")
    message = input("> ")
    loadingBar(prefix = 'Checking Input:', length = 20)
    return determine_input(message)


def determine_input(message):
    if (message in query_commands):
        return handle_query()
    elif (message in help_commands):
        return handle_help()
    elif (message in exit_commands):
        return handle_exit()
    else:
        return handle_unknown()
    
def handle_unknown():
    print("""UNKNOWN COMMAND
    FOR A LIST OF KNOWN COMMANDS, TYPE HELP
    """)
    return await_command()
    
def handle_help():
    print("""KNOWN COMMANDS:
        [HELP] LIST KNOWN COMMANDS
        [QUERY] ASK DERO A QUESTION
        [STATEMENT] ISSUE A COMMAND, SUCH AS SETTING A TIMER, RETRIEVING DATA, OR STORING DATA
        [EXIT] CLOSE THE DERO PROGRAM
          
        FORMAT COMMANDS SEPARATED BY A COLON, AS FOLLOWS:
        KEYWORD: REQUEST
          
    """)
    return await_command()
    
def handle_query():
    return await_command()

def handle_exit():
    print("""EXIT COMMAND REGISTERED
          GOODBYE
    """)
    return False

def handle_command():
    return await_command()