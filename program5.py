#Question 5: Robust File Management and Directory Navigation Utility
import os
import sys

# Check command-line arguments
if len(sys.argv) < 2:
    print("Usage: python file_manager.py <command>")
    print("Commands: list, create, read, workspace")
    sys.exit()

command = sys.argv[1]

# 1. List files and folders
if command == "list":
    path = os.getcwd()

    print("\nCurrent Directory:", path)
    print("\nContents:")

    for item in os.listdir(path):
        print(item)


# 2. Create a workspace folder
elif command == "workspace":
    folder_name = input("Enter workspace folder name: ")

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("Workspace created:", folder_name)
    else:
        print("Workspace already exists.")


# 3. Read a text file
elif command == "read":
    filename = input("Enter text file name: ")

    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()

        print("\nFile Content:")
        print(content)
    else:
        print("File does not exist.")


# 4. Create a text log file
elif command == "create":
    filename = input("Enter log file name: ")

    with open(filename, "w") as file:
        message = input("Enter log message: ")
        file.write(message)

    print("Log file created successfully.")


else:
    print("Invalid command.")