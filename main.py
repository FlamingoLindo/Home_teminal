import os
import time

import subprocess
import sys

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), 'Functions'))

from Functions.General import *

from Functions.Work import *
from Functions.Home import *

def show_home_commands():
    """Show Home commands."""
    clear_console()
    while True:
        clear_console()
        print("[1] Firefox tabs \n[2] Nothing here \n[3] Percentage \n[4] Youtube Downloader \n[5] Back to Main Menu")
        command = input("Command: ").strip().lower()

        if command == "1":
            print("Opening all links...")
            open_all_links()
            clear_console()
        elif command == "2":
            print("Nothing here...")
            time.sleep(1)
            clear_console()
        elif command == "3":
            clear_console()
            percentage()
        elif command == "4":
            clear_console()
            downloader()
        elif command == "5":
            clear_console()
            return
        else:
            print("Unknown command. Please enter a valid option.")

def show_work_commands():
    """Show Work commands."""
    clear_console()
    while True:
        print("[1] Open Asana Links \n[2] Open Websites \n[3] Start Appium server \n[4] Start adb \n[5] Open generators \n[6] Back to Main Menu")
        command = input("Command: ").strip().lower()

        if command == "1":
            print("Opening Asana tabs links...")
            open_multiple_asana_links()
            clear_console()
        elif command == "2":
            print("Opening tabs...")
            open_project_tabs()
            clear_console()
        elif command == "3":
            print("Starting Appium server...")
            clear_console()
            start_appium()
        elif command == "4":
            print("Starting adb...")
            clear_console()
            start_adb()
        elif command == "5":
            print("Opening tabs...")
            open_gen_tabs()
            clear_console()
        elif command == "6":
            clear_console()
            return
        else:
            print("Unknown command. Please enter a valid option.")

def main():
    load_intro()
    """Main function to run the application."""
    command_actions = {
        "1": show_home_commands,
        "2": show_work_commands,
    }
    
    while True:
        clear_console()
        day()
        print("\n[1] Home \n[2] Work \n[3] Exit")

        command = input("Command: ").strip().lower()
        
        if command == "3":
            print("\nExiting the application.")
            clear_console()
            break
        elif command in command_actions:
            command_actions[command]()
        else:
            print("Unknown command. Please enter a valid option.")

if __name__ == "__main__":
    main()
