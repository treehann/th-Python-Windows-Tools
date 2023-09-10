import os

def replace_character_in_filenames(directory, old_char, new_char):
    for filename in os.listdir(directory):
        if old_char in filename:
            new_filename = filename.replace(old_char, new_char)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    old_char = input("Enter the string to be replaced: ")
    new_char = input("Enter the string to replace it with: ")
    replace_character_in_filenames(".", old_char, new_char)
