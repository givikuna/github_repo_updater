import os
import subprocess

def git_pull():
    subprocess.run(["git", "pull"])

def process_folders(directory):
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder}")
            current_dir = os.getcwd()
            os.chdir(folder_path)
            git_pull()
            os.chdir(current_dir)
            print(f"Finished processing folder: {folder}\n")

process_folders(os.getcwd())
