import os
import platform

def clear_console():
    """Clear the console based on the operating system."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def open_url(url):
    """Open a URL in the default web browser"""
    try:
        os.system(f"start chrome {url}")
    except Exception as e:
        print(f"Failed to open URL {url}. Error: {e}")

def open_multiple_asana_links():
    """Open multiple Asana links."""
    asana_urls = [
        "https://app.asana.com/0/1207221290310617/1207225690268341",
        "https://app.asana.com/0/1207504713283391/1207504634680432",
        "https://app.asana.com/0/1207747544851675/1207747639592319",
        "https://app.asana.com/0/1207933859745403/1207934164249687",
        "https://app.asana.com/0/1206990839359887/1206991821570634",
        "https://app.asana.com/0/1207990406862834/1207991814209722",
        "https://www.notion.so/work-esteralvim/APRESENTA-O-MOTORFIND-INTEGRA-O-faea137f72eb4f26b02ae95e685ba519?pvs=11"
    ]

    for asana in asana_urls:
        print(f"Opening {asana}...")
        open_url(asana)
        
def open_project_tabs():
    """Open multiple Asana links."""
    prject_tabs = [
        "https://motorfind-client.netlify.app/",
        "https://motorfind-master.netlify.app/",
        "https://crm-mestres-web-v2024.netlify.app/",
        "https://saas-64327.bubbleapps.io/pagina_inicial"
    ]

    for tab in prject_tabs:
        print(f"Opening {tab}...")
        open_url(tab)

def show_home_commands():
    """Show Home commands."""
    clear_console()
    print("Displaying Home commands...")
    # Add additional home-related logic here

def show_work_commands():
    """Show Work commands."""
    clear_console()
    while True:
        print("[1] Open Asana Links \n[2] Open Websites \n[3] Back to Main Menu")
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
            clear_console()
            return
        else:
            print("Unknown command. Please enter a valid option.")

def main():
    """Main function to run the application."""
    command_actions = {
        "1": show_home_commands,
        "2": show_work_commands,
    }

    while True:
        print("[1] Home \n[2] Work \n[3] Exit")
        command = input("Command: ").strip().lower()

        if command == "3":
            print("\nExiting the application.")
            break
        elif command in command_actions:
            command_actions[command]()
        else:
            print("Unknown command. Please enter a valid option.")

if __name__ == "__main__":
    main()
