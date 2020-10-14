class Queue:
  def __init__(self, capacity):
        self.internalArray = [None] * self.capacity
        self.front = 0
        self.back = 0
        self.capacity = 5
  
  
  def add (self, item):
    #pass
    self.internalArray[self.back] = item
    self.back += 1
  
  def remove(self):
    pass

  def __str__(self):
    pass