"""
Bonus Challenge (Optional): FizzBuzz Game

Print numbers from 1 to 50.
If a number is divisible by 3, print "Fizz".
If a number is divisible by 5, print "Buzz".
If a number is divisible by both 3 and 5, print "FizzBuzz".
"""
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"{i} FizzBuzz!")
    elif i%5==0:
        print(f"{i} Buzz")
    elif i%3==0:
        print(f"{i} Fizz")
    else:
        print(i)
    