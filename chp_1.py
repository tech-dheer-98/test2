import os

# Specify the current folder name and the new folder name
current_folder = "old_folder_name"  # Replace with the current folder name
new_folder = "new_folder_name"      # Replace with the desired new folder name

# Rename the folder
try:
    os.rename(current_folder, new_folder)
    print(f"Folder renamed successfully from {current_folder} to {new_folder}")
except FileNotFoundError:
    print(f"The folder {current_folder} does not exist.")
except PermissionError:
    print("Permission denied. Ensure you have the proper permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
