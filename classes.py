class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # Code to add an item to the stack will go here
      self.internalArray.append(item)

    def pop(self):
      
      if len(self.internalArray) == 0:
        print ("Stack is empty - cannot pop")
      else:
        a = self.internalArray[-1]
      
        # Code to remove an item from the top of the stack will go here 
        del self.internalArray[-1]
        return a

    def __str__(self):
        return self.internalArray.__str__()

stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)

popped1 = stack1.pop()
print(popped1)
popped2 = stack1.pop()
print(popped2)
popped3 = stack1.pop()
print(popped3)
popped4 = stack1.pop()
if not popped4 is None:
  print(popped4)

class Stack1:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # Code to add an item to the stack will go here
        self.internalArray.append(item)
    def pop(self):
        # Code to remove an item from the top of the stack will go here 
      print("")
    def __str__(self):
        return self.internalArray.__str__()
