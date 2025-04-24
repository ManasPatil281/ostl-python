import os

# Function to create, modify, display, and delete files and directories
def main():
    # Create a file (if it does not exist)
    try:
        with open("file_create.txt", "w") as file:
            file.write("Hello to the world!!")
        print("File created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")
        return

    # Modify the contents (append to the file)
    try:
        with open("file_create.txt", "a") as file:
            file.write(" New content")
        print("File modified successfully.")
    except IOError as e:
        print(f"Error modifying file: {e}")
        return

    # Create a directory
    try:
        os.mkdir("new_dir")
        print("Directory 'new_dir' created successfully.")
    except FileExistsError:
        print("Directory 'new_dir' already exists.")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Delete the file
    try:
        os.remove("file_create.txt")
        print("File 'file_create.txt' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")
        return

    # Delete the directory
    try:
        os.rmdir("new_dir")
        print("Directory 'new_dir' deleted successfully.")
    except OSError as e:
        print(f"Error deleting directory: {e}")
        return

    # Display the contents of the file (recreate the file first)
    try:
        with open("file_create.txt", "w") as file:
            file.write("Hello to the world!!")
            file.write(" New content")
        print("\nContents of the file:")
        
        with open("file_create.txt", "r") as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"Error reading or writing file: {e}")
        return


if __name__ == "__main__":
    main()
