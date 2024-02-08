#Exception handling

#SyntaxError 

# str = "Exception Handling"

# for s in str:
#     if(s != p :
#        print(s)

#NameError
# str = "Exception Handling"

# for s in str:
#     if(s != p) :
#        print(s)

try:
    fh = open("Textfile.txt", "w")
    fh.write("This is my textfile for Exception Handling.")
except IOError:
    print("Error can\'t find file or read data")
else:
    print("Written content in the file successfully...")
    fh.close()