# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and write to the file
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: The number is 42.\n")
            file.write("Line 3: Python is fun.\n")
        print("File created and initial lines written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred during file creation and writing: {e}")
    finally:
        print("Create and write operation complete.")


def read_and_display_file():
    try:
        # Read the file and display contents
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred during file reading: {e}")
    finally:
        print("Read operation complete.")


def append_to_file():
    try:
        # Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("Line 4: Adding more text.\n")
            file.write("Line 5: The answer is still 42.\n")
            file.write("Line 6: Keep learning Python!\n")
        print("Additional lines appended.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred during file appending: {e}")
    finally:
        print("Append operation complete.")


if __name__ == '__main__':
    # Create and write to the file
    create_and_write_file()
    
    # Read and display the file contents
    read_and_display_file()
    
    # Append more lines to the file
    append_to_file()
    
    # Read and display the file contents again to confirm append
    read_and_display_file()
