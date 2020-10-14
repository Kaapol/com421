class Node:
  def __init__(self, data):
      # A node has 3 attributes
      # data - the actual data stored in the node
      # next - the link to the next node
      # prev - the link to the previous node
      self.data = data
      self.next = None
      self.prev = None

  def link(self, otherNode):
    self.next = otherNode
    otherNode.prev = self

    
  
  def __str__(self):
    return self.data.__str__()

class LinkedList:
  def __init__(self):
    self.first = None
    self.last = None
  
  def add(self, Node):
    if (self.first is None):
      self.first = Node
    else:
      self.last.link(Node)
    
    self.last = Node
  
  def get(self, index):
    counter = 0
    currentNode = self.first
    while currentNode is not None and counter < index:
      counter += 1
      currentNode = currentNode.next
    
    return currentNode


#Main program
n1 = Node ("Apple")
n2 = Node ("Orange")

print(n1)
print(n2)

n1.link(n2)
#n2.link(n1)

print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)