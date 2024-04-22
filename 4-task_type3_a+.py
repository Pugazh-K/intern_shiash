# task 4: Use of r+ w+ a+ in python file handling

# “a+” (Append and Read):
""" Opens the file for appending (writing at the end) and reading.
    Creates a new file if it doesn’t exist."""
#Example

with open ("C:\\Users\pugaz\OneDrive\Documents\my_file_new2.txt", "a+") as file:
    file.write("I am Pugazh")
    file.seek(0)
    content = file.read()
    print(content)