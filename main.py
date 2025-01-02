
from commands import exit_commands, loadingBar
from menu import boot

def main():
    # Start an infinite loop to keep the chatbot running.
    while True:
        # Ask the user to enter a message or 'exit' to leave.
        message = boot()
        
        # Check if the message is 'exit', to end the loop and shut down the chatbot.
        if message == False:
            break  # Breaks the loop, ending the function and closing the chatbot.


if __name__ == "__main__":
    main()