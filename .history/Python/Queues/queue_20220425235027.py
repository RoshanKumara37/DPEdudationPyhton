#Creating Queue For Add Value to the List
def enqueue (queue,value):#enqueue -> enter value to queue
    queue.append(value)

#Creating Queue For Remove Value from the List
def dequeue(queue):#dequeue -> delete value from queue
    return queue.pop()

myList = []
print(myList)
enqueue(myList,5)
enqueue(myList,7)
print(myList)
dequeue(myList)
print(myList)