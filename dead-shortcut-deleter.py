import os
import pylnk3

def is_shortcut_invalid(lnk_path):
    try:
        # If the linked file doesn't exist, then the shortcut is considered invalid
        linked_file = pylnk3.parse(lnk_path)
        if not os.path.exists(linked_file.path):
            return True
    except Exception as e:
        # Any issue in parsing the lnk or accessing its properties can be treated as invalid
        print(f"Error processing {lnk_path}: {e}")
        return True
    return False

def main():
    current_directory = os.getcwd()
    deleted_count = 0
    
    for file in os.listdir(current_directory):
        if file.endswith(".lnk"):
            full_path = os.path.join(current_directory, file)
            if is_shortcut_invalid(full_path):
                os.remove(full_path)
                deleted_count += 1
                print(f"Deleted invalid shortcut: {file}")

    print(f"\nTotal shortcuts deleted: {deleted_count}")
    input("Press any key to continue...")

if __name__ == "__main__":
    main()
