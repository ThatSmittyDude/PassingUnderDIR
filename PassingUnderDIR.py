import os
import shutil
import zipfile
import subprocess

def display_directory_contents(path='.'):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f'[{entry.name}]')
            else:
                print(entry.name)

def display_help():
    print("\nAvailable commands:")
    print("  help                       - Display this help message")
    print("  exit                       - Quit the program")
    print("  [folder]                   - Change to the specified folder")
    print("  ..                         - Move up one level")
    print("  copy [source] [destination]- Copy file from source to destination")
    print("  rename [old_name] [new_name]- Rename file from old_name to new_name")
    print("  delete [file]              - Delete the specified file")
    print("  unzip [zip_file] [folder]  - Unzip the contents of a zip file to a folder")
    print("  open [file]                - Open the specified file with the default program")

if __name__ == "__main__":
    current_directory = os.getcwd()

    while True:
        print(f"\nCurrent Directory: {current_directory}")
        display_directory_contents(current_directory)

        command = input("\nEnter a command (or 'exit' to quit): ").strip()

        if command.lower() == 'exit':
            break
        elif command.lower() == 'help':
            display_help()
        else:
            try:
                if command.startswith('copy'):
                    _, source, destination = command.split(' ')
                    shutil.copy(os.path.join(current_directory, source), os.path.join(current_directory, destination))
                elif command.startswith('rename'):
                    _, old_name, new_name = command.split(' ')
                    os.rename(os.path.join(current_directory, old_name), os.path.join(current_directory, new_name))
                elif command.startswith('delete'):
                    _, file_name = command.split(' ')
                    os.remove(os.path.join(current_directory, file_name))
                elif command.startswith('unzip'):
                    _, zip_file, extract_folder = command.split(' ')
                    with zipfile.ZipFile(os.path.join(current_directory, zip_file), 'r') as zip_ref:
                        zip_ref.extractall(os.path.join(current_directory, extract_folder))
                elif command.startswith('open'):
                    _, file_name = command.split(' ')
                    subprocess.run(['start', os.path.join(current_directory, file_name)], shell=True)
                elif os.path.isdir(os.path.join(current_directory, command)):
                    current_directory = os.path.join(current_directory, command)
                elif command == '..':
                    current_directory = os.path.dirname(current_directory)
                else:
                    print("Invalid command. Enter 'help' for a list of commands.")
            except Exception as e:
                print(f"An error occurred: {e}")



        # -*- coding: utf-8 -*-
"""
       Created on Thu Dec 14 19:20:59 2023

       @author: Austin Smith
                ThatSmittyDude@outlook.com
                passingunderyellow.com
                puyinside.com
                aurinside.com
                """