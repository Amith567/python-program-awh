"""
Task 5.4: Implement Exception Handling

Modify your program to:

✔ Use a try-except block to handle:

File not found errors (FileNotFoundError).

Permission issues (PermissionError).

Any other unexpected errors.
"""
try:
    with open("new.txt","w")as file:
        for i in range(5):
            file.write(input("Enter name : ")+"\n")
    
    with open("new.txt","r")as file:
        content=file.read()
    print(content)
except FileNotFoundError:
    print("the file not found")
except PermissionError:
    print("no permission")
except Exception as e:
    print(f"unexpected exception occured {e}")
    

    
