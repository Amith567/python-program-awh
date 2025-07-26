"""
Task 4.5: Reverse Each Word in a Sentence

Write a function that:

Takes a sentence as input.
Reverses each word while keeping their order intact.
"""
inp=input("Enter a sentence : ")
lis=inp.split()
lista=[]
for word in lis:
    new=word[::-1]
    lista.append(new)

print(" ".join(lista))
