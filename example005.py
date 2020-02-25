import os

def new_directory(directory, filename):
# Before creating a new directory, check to see if it already exists

    if not os.path.exists(directory):
        os.mkdir(directory)
        os.chdir(directory)
        with open(filename, "w") as file:
            file.write("")
        os.chdir("..")
    return os.listdir(directory)

# Create the new file inside of the new directory

# Return the list of files in the new directory

print(new_directory("PythonPrograms", "script.py"))