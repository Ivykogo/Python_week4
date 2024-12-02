import os
def read_and_modify_file():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, 'r') as file:
            content = file.readlines()
            
        modified_content = [f"{i + 1}:) {line}" for i, line in enumerate(content)]
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)
        
        print(f"Modified content written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError as e:
        print(f"Error: Unable to read or write files. {e}")
read_and_modify_file()
