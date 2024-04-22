# task 4: Use of r+ w+ a+ in python file handling

# “w+” (Write and Read):
""" This mode truncates the file (clears its content) if it exists, 
    or creates a new file.
    It’s useful for creating or overwriting files. """
#Example

with open ("C:\\Users\pugaz\OneDrive\Documents\my_file_new.txt", "w+") as file:
    file.write("I am Pugazhendhi")
    file.seek(0)
    content = file.read()
    
    print(content)