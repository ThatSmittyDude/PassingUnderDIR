# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 20:02:18 2023

@author: smith
"""

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
    print("  mkdir [folder]             - Create a new folder")
    print("  rmdir [folder]             - Delete the specified folder")

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")
    except PermissionError:
        print(f"Permission denied. Make sure the folder is not in use by another process.")

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
                elif command.startswith('mkdir'):
                    _, folder_name = command.split(' ')
                    create_folder(os.path.join(current_directory, folder_name))
                elif command.startswith('rmdir'):
                    _, folder_name = command.split(' ')
                    delete_folder(os.path.join(current_directory, folder_name))
                else:
                    print("Invalid command. Enter 'help' for a list of commands.")
            except Exception as e:
                print(f"An error occurred: {e}")
