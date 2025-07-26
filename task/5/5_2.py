"""
Task 5.2: Read from the File

Modify the program to:

✔ Open students.txt in read mode (r).
✔ Read and print the entire content of the file.
"""
file=open("new.txt","r")
content=file.read()
print(content)
file.close()