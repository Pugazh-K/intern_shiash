# task 4: Use of r+ w+ a+ in python file handling

# “r+” (Read and Write):
""" In this mode, you can read from and write to an existing file.
    If the file doesn’t exist, 
    it raises an error. """
#Example

with open("C:\\Users\pugaz\OneDrive\Documents\my_file.txt", "r+") as file:
    content = file.read()  
    file.write("\nAppending new content!") 
    file.seek(0)
    file.write("Overwriting existing content")
    print(content)

