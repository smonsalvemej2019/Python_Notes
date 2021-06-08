#file handling is an important part of any coding language
#python allows us to create,read,update,and delete files

#firs we have to open the file using the keyword "open(<name of file>,<mode>)"
#the modes are the following:
# "r" read, default and returns error if file does not exist
# "a" Append, open file for append, creates file if it does not exist
# "w" write, open file for writing, creates file if it does not exist
# "x" creates file if it does not exist, returns error if file exist

#we can also handle the file as text "t" or binary "b"

file = open("files/demo.txt", "rt")#we do not need rt because those are defaults

#if we print file as it is right now, it will output the information of the open() function
#but not the content of the file.

print("\nFile open info:", file)

#to read the content of a file we use special methods 

print("File content:",file.read())
file.close()


#we can read individual lines as well
file = open("files/demo.txt", "rt")
print("\n\n")
print(file.readline())#first line
print(file.readline())#second line
file.close()

#we can also loop trough lines
file = open("files/demo.txt", "rt")
print("\n\n")
for lines in file: print(lines)
file.close()

#we can specify how many characters we want
file = open("files/demo.txt", "rt")
print("\n\n")
print(file.read(4))
file.close()

#writing on files is an important of any coding language\
file = open("files/demo.txt", "a")#first we set on append
#append will ADD to a file write will OVERWRITE
file.write("Ohh more content!!!")
file.close()

print("\n\n")
file = open("files/demo.txt")
print(file.read())




