import os

def list_files_in_directory():
    files = os.listdir()
    if files:
        print("Files in the current directory:")
        for file in files:
            print(file)
    else:
        print("The current directory is empty.")

def make_file(filename):
    try:
        with open(filename, 'w'):
            print(f"File '{filename}' created successfully.")
    except OSError:
        print(f"Failed to create file '{filename}'.")

def make_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except OSError:
        print(f"Failed to create directory '{directory_name}'.")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except OSError:
        print(f"Failed to delete file '{filename}'.")

def delete_file_in_directory(directory, filename):
    try:
        os.remove(os.path.join(directory, filename))
        print(f"File '{filename}' deleted successfully from directory '{directory}'.")
    except OSError:
        print(f"Failed to delete file '{filename}' from directory '{directory}'.")

def process_command(command):
    if "list files" in command:
        list_files_in_directory()
    elif "make file" in command or "create file" in command:
        filename = command.split("called")[1].strip()
        make_file(filename)
    elif "make directory" in command or "create directory" in command:
        directory_name = command.split("named")[1].strip()
        make_directory(directory_name)
    elif "delete file" in command:
        filename = command.split("called")[1].strip()
        delete_file(filename)
    elif "delete file in directory" in command:
        directory = command.split("directory")[1].split("called")[0].strip()
        filename = command.split("called")[1].strip()
        delete_file_in_directory(directory, filename)
    else:
        print("Command not recognized.")

# Main program loop
while True:
	
    command = input('Enter your command: ');    

    if command:
        if "exit" in command:
            print("Exiting the program.")
            break
        process_command(command)
