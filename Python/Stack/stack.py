from multiprocessing.sharedctypes import Value
from tkinter import N

#Creating Stack For Add Value to the list
def push (stack,value):
    stack.append(value)

#Creating Stack For Remove Value from the list
def pop(stack):
    return stack.pop()

# myList = []
# push(myList,5)
# print(myList)
# pop(myList)
# print(myList)

#Created List Using Stack and add square values
squareNumbers = []
n=0
while(n<100):
    n+=1
    numberText = str(n) + " * "+ str(n) + " = " + str(n*n)
    push(squareNumbers,numberText)
    print(numberText)
print(squareNumbers)



