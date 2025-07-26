"""Extend the program to:

✔ Open students.txt in append mode (a).
✔ Add three more student names to the file.
✔ Close the file after appending.
"""
file=open("new.txt","a")
for i in range(3):
    file.write(input("enter the name : ")+"\n")
file.close()