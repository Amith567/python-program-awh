"""
Task 3.5: Password Guessing Game (Using while loop)

Write a program that:

Sets a secret password (e.g., "python123").
Asks the user to guess the password in a loop.
If the guess is incorrect, it asks again.
If the guess is correct, print "Access Granted" and exit the loop.
"""
password=546
guess=0
while password!=guess:
    guess=int(input("enter a three digit number : "))
print("congragulations for successfully guess the number !")