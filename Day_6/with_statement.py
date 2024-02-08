file = "Textfile.txt"
# print("The lines of the given statement are: ")

with open(file, "r") as filedata:
    filelines = filedata.readlines()
    for textline in filelines:
        print(textline)



# inputFile = open("Textfile.txt", "a")


# #try-except block..
# try:
#    inputFile.write("\nHello python")
# finally:
#    inputFile.close()

# #replacing try except blocking by with statement

# File = "Textfile.txt"
# with open(File, "a") as file1:
#     file1.write("\nHello by replacing try-except by with statement...")