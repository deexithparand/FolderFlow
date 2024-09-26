import os

def print_folder_structure(folder_path, prefix=""):
    contents = os.listdir(folder_path)
    contents.sort()  # To ensure contents are printed in order

    for index, item in enumerate(contents):
        item_path = os.path.join(folder_path, item)

        # Ignore hidden files and directories (starting with a dot)
        if item.startswith('.'):
            continue

        if index == len(contents) - 1:
            connector = "└── "
            new_prefix = prefix + "    "
        else:
            connector = "├── "
            new_prefix = prefix + "│   "

        print(prefix + connector + item)

        if os.path.isdir(item_path):
            print_folder_structure(item_path, new_prefix)

# Get the current working directory
folder_path = os.getcwd()
print(os.path.basename(folder_path) + "/")
print_folder_structure(folder_path)

