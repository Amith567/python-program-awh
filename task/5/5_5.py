"""
Task 5.5: Count the Number of Lines in the File

Write a function count_lines() that:

✔ Opens students.txt in read mode (r).
✔ Counts and prints the total number of lines (students) in the file."""

with open("new.txt","r")as file:
    lines=file.readlines()
print(f"no of lines : {len(lines)}")