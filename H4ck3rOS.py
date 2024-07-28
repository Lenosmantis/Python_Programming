import getpass
import os
import subprocess
import time

current_version = 1.0

def auto_update_command():
    global current_version
    print("\nChecking for updates...")
    time.sleep(2)
    print("Loading", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

    new_version = 2.0
    if current_version < new_version:
        print(f"A newer version ({new_version}) is available.")
        answer = input("Would you like to upgrade? (y/n): ").lower()
        if answer == "y":
            print("H4ck3rOS updated to version 2.0")
            current_version = new_version
        else:
            print("Upgrade cancelled.")
    else:
        print("You already have the latest version of H4ck3rOS.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_command():
    print("Exiting H4ck3rOS. Goodbye!")
    with open("hacker_logs.txt", "a") as f:
        f.write(f"Logout - Time: {time.ctime()}\n")
    exit()

def help_command():
    print("\nAvailable commands:")
    print(" - version: Display the current and previous version of the terminal")
    print(" - auto_update: Check for updates")
    print(" - clear: Clear the terminal")
    print(" - exit: Exit H4ck3rOS")
    print(" - help: Display this list of commands")
    print(" - install_app: Install a third-party app")
    print(" - malware: Execute malware")
    print(" - notifications: Send a notification message")
    print(" - search: Search for files or information")

def install_app_command():
    app_name = input("Enter the name of the third-party app to install: ")
    print("Installing", app_name, "...")
    time.sleep(3)
    print(app_name, "installed successfully.")

def loading_progress():
    print("Starting H4ck3rOS...")
    time.sleep(2)

def login():
    print("Login to H4ck3rOS")
    try:
        username = input("Enter username: ")
        password = getpass.getpass("Please enter your secret password to start H4ck3rOS: ")
    except KeyboardInterrupt:
        print("\nLogin interrupted. Exiting H4ck3rOS.")
        exit()

    with open("hacker_accounts.txt", "r") as f:
        lines = f.readlines()
        credentials = [line.strip().split() for line in lines]
        if [username, password] in credentials:
            print("Login successful!")
            with open("hacker_logs.txt", "a") as history_file:
                history_file.write(f"Login - Username: {username}, Time: {time.ctime()}\n")
            return True
        else:
            print("Invalid username or password.")
            return False

def malware_command():
    print("Downloading malware...")
    time.sleep(2)
    print("Installing malware...")
    time.sleep(2)
    print("Executing malware...")
    time.sleep(1)
    actions = ["Corrupting files...", "Deleting important data...", "Encrypting files...", "Sending spam emails..."]
    for action in actions:
        print(action)
        time.sleep(2)
    print("Malware execution complete.")

def notifications_command():
    message = input("Enter notification message: ")
    print("Notification:", message)

def search_command():
    print("Searching...")
    time.sleep(2)
    print("Welcome to Search!")
    search_term = input("Enter search term: ")
    home_path = "/data/data/com.termux/"
    results = []
    for root, dirs, files in os.walk(home_path):
        for file in files:
            if search_term in file:
                results.append(os.path.join(root, file))
    if results:
        print("Search results:")
        for result in results:
            print("- " + result)
    else:
        print("No results found.")

def sign_up():
    print("Sign up for H4ck3rOS")
    username = input("Enter new username: ")
    password = getpass.getpass("Enter new secret password: ")

    with open("hacker_accounts.txt", "a") as f:
        f.write(f"{username} {password}\n")
    print("Account created successfully!")

    with open("secret_password.txt", "w") as f:
        f.write(password)

def version_command():
    print("Previous version:", current_version - 1.0)
    print("Current version:", current_version)

def main():
    # Check if secret password file exists, if not, create it
    if not os.path.exists("secret_password.txt"):
        sign_up()

    # Check if startup_os.txt file exists and contains the correct secret password
    if not os.path.exists("startup_os.txt"):
        print("Error: Startup file 'startup_os.txt' not found.")
        exit()
    else:
        with open("startup_os.txt", "r") as f:
            startup_password = f.read().strip()
            if startup_password != "T3rm&uxP@ssw0rd!":
                print("Error: Incorrect secret password in startup file.")
                exit()

    while True:
        choice = input("Welcome to H4ck3rOS! Would you like to (1) login or (2) sign up? ").lower()
        if choice == "1" or choice == "login":
            if login():
                break
        elif choice == "2" or choice == "sign up":
            sign_up()
        else:
            print("Invalid choice. Please try again.")

    while True:
        loading_progress()

        while True:
            command = input("H4ck3rOS> ").lower()

            if command == "version":
                version_command()
            elif command == "help":
                help_command()
            elif command == "exit":
                exit_command()
            elif command == "search":
                search_command()
            elif command == "auto_update":
                auto_update_command()
            elif command == "notifications":
                notifications_command()
            elif command == "install_app":
                install_app_command()
            elif command == "malware":
                malware_command()
            elif command == "clear":
                clear_terminal()
            else:
                print("Command not recognized. Type 'help' for assistance.")

if __name__ == "__main__":
    main()
