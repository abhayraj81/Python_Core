# File Handling

# mode: r-read, w-write, a-append

# open file
file = open('example.txt','r')


# Read File

print("--Read File--")

file = open('example.txt','r')
content = file.read()   # read entire data
print(content)
file.close() 


# Read first line

print("--Read First Line--")

file = open('example.txt','r')
content = file.readline()   # read first line
print(content)
file.close() 


# Read file using Readlines()

print("--Using Readlines()--")

file = open('example.txt','r')
content = file.readlines()   # list entire data
print(content)
file.close() 