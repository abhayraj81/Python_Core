# write to a file

# 'w' - write mode 
# write to a file and over write to a file

file = open('example1.txt','w')     
file.write("Namasteee !!!, data is overwritten")
file.close()


# 'a' - append mode
# append data to file and incremental data to file

file = open('example1.txt','a')     
file.write("\nI am new world sega")
file.close()


# close a file

# using with statement
with open('example1.txt','r') as file:
    content = file.read()
    print(content)

    