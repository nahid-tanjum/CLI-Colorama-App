import sys
import time
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init()

def slow_print(text, delay=0.05):
    """Print text with a delay to create a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def greeting(name):
    """Greet the user with a formatted welcome message."""
    slow_print(Fore.CYAN + f"\nWelcome, {name}!" + Style.RESET_ALL)
    slow_print(Fore.YELLOW + "We're happy to have you in the Docker CLI app." + Style.RESET_ALL)
    slow_print(Fore.GREEN + "\nHere's what you can do with this app:" + Style.RESET_ALL)
    slow_print(Fore.GREEN + "- Receive a warm greeting" + Style.RESET_ALL)
    slow_print(Fore.GREEN + "- Enjoy a beautifully styled CLI experience\n" + Style.RESET_ALL)

def main():
    slow_print(Fore.BLUE + "========== Welcome to Nahid Tanjum's CLI App ==========" + Style.RESET_ALL)
    
    if len(sys.argv) > 1:
        name = sys.argv[1]
        greeting(name)
    else:
        slow_print(Fore.RED + "\nIt seems you forgot to provide your name." + Style.RESET_ALL)
        slow_print(Fore.CYAN + "Please run the app again with your name like this:" + Style.RESET_ALL)
        slow_print(Fore.YELLOW + "   docker run mycliapp YourName" + Style.RESET_ALL)
        slow_print(Fore.CYAN + "\nFor now, we'll greet you anonymously.\n" + Style.RESET_ALL)
        greeting("Anonymous User")

if __name__ == '__main__':
    main()
