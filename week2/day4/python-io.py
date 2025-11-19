import os

# Python I/O

# Old school way: you need to explicity close the file after using it - using close() method

# file_obj = open("file-name.txt", "w")
# # your code to do anything you want
# file_obj.close()      

# new way: use with statement

# with open ("secrets.txt", "r") as file_obj: # FileNotFoundError: [Errno 2] No such file or directory: 'secrets.txt'
#     print(file_obj.read())

# solution for FileNotFoundError = use os model to give the full path to the file
dir_path = os.path.dirname(os.path.realpath(__file__))

# with open (dir_path + "\secrets.txt", "r") as file_obj: # FileNotFoundError: [Errno 2] No such file or directory: 'secrets.txt'
#     content = file_obj.read()
#     print(content)

# Methods:

# f.read() 
# f.readline() - Reads one entire line from the file. Reads a file till the newline
# f.readlines() - Reads a file line by line, returns a list of the lines in the file

# f.write(str) 
# f.writelines(seq) - Writes a list of lines to the file.
# Example : 
# lines=["Hello world.\n", "Welcome to Paris.\n"]
# f.writelines(lines)

# f.tell() - get the current file position
# f.seek(0) - bring file cursor to initial position

# EXERCISE:
# Read the file line by line

with open(dir_path + "\starwars.txt", "r+") as f:
    txt_list = f.readlines()
    for line in txt_list:
        print(line)
    print("End of document")

# Read only the 5th line of the file
    # print(txt_list[4])
    
# Read only the 5 first characters of the file
    print(txt_list[:5])

# Read all the file and return it as a list of strings. Then split each word into letters
    temp = [] # step 1 created a emplty list
    for name in txt_list: # step 2 for loop 
        temp.append(list(name)) # step 3 append name at the list

    print(temp)

    # list comprehension 
    temp = [list(name) for name in txt_list] # stesso risultato del passaggio sopra
    print(temp)
    

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
    # counts = {"Darth": 0, "Luke": 0, "Lea": 0}
    # for name in txt_list:
    #     if name == "Darth":
    #         counts["Darth"] += 1
    #     elif name == "Luke":
    #         counts["Luke"] += 1
    #     elif name == "Lea":
    #         counts["Lea"] += 1
    # print(counts)

    # There is a better way: use count()
    full_txt_str = "".join(txt_list)
    counts = {"Darth": full_txt_str.count("Darth"), 
              "Luke": full_txt_str.count("Luke"), 
              "Lea": full_txt_str.count("Lea")
              }
    print(counts)

# Append your first name at the end of the file
with open(dir_path + "\starwars.txt", "a+") as f:
    f.seek(0, os.SEEK_END)
    f.write("\nGIovanni")
    print("Successfully added")

# Append "SkyWalker" next to each first name "Luke"
with open(dir_path + "\starwars.txt", "r+") as f:
    txt_list = f.readlines()
    modified_content = []
    for name in txt_list:
        if name == "Luke\n":
            modified_content.append("Luke SkyWalker\n")
        else:
            modified_content.append(name)

    print(modified_content)


with open(dir_path + "\starwars.txt", "w") as f:
    f.seek(0)
    f.writelines(modified_content)
    print("SkyWalker successfully added")
    