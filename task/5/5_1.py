"""
Task 5.1: Create and Write to a File

Write a Python program that:

✔ Creates a text file named students.txt.
✔ Writes at least five student names, each on a new line.
✔ Closes the file properly after writing.
"""
file=open("new.txt","w")
for i in range(5):

    file.write(input("Enter name : ")+"\n")
file.close()
# file=open("new.txt","r")
# content=file.read()
# print(content)
# file.close()
