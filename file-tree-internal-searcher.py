import os

def find_string_in_file(filename, search_string):
    """Check if the search string is present in the file."""
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        return search_string in content

def search_files_in_directory(directory, search_string):
    """Search for the string in all files in the directory and its subdirectories."""
    matching_files = []

    # Walk through root, directories and files in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            full_path = os.path.join(root, filename)
            if find_string_in_file(full_path, search_string):
                matching_files.append(full_path)

    return matching_files

def main():
    # Define the folder from which the Python file was run as the working directory (WD)
    working_directory = os.getcwd()

    # Prompt the user for a string
    search_string = input("Please enter the string you're searching for: ")

    # Search for the string inside all files in the WD and its subdirectories
    matching_files = search_files_in_directory(working_directory, search_string)

    # Print out a list of all file paths to matching files
    if matching_files:
        print("\nMatching files are:")
        for file in matching_files:
            print(file)
    else:
        print("\nNo matching files found.")

    # Prompt for "press any key..." at the end
    input("\nPress any key to continue...")

if __name__ == '__main__':
    main()
