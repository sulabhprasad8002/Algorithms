class Node():
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class binarysearchtree():
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    newnode = Node(value)
    
    if self.root == None:
      self.root = newnode
    else:
      currentnode = self.root

      while True:
        if value < currentnode.value:
          if not currentnode.left:
            currentnode.left = newnode
            return self
          
          currentnode = currentnode.left
        
        if value > currentnode.value:
          if not currentnode.right:
            currentnode.right = newnode
            return self

          currentnode = currentnode.right
  
  def lookup(self, value):
    if not self.root:
      return None
    
    currentnode = self.root

    while currentnode:
      if value < currentnode.value:
        currentnode = currentnode.left
      elif value > currentnode.value:
        currentnode = currentnode.right
      elif value == currentnode.value:
        return currentnode
    
    return None

  def breadthfirstsearch(self):
    currentnode = self.root
    list = []
    queue = []
    queue.append(currentnode)

    while len(queue) > 0:
      currentnode = queue.pop(0)
      list.append(currentnode.value)

      if currentnode.left:
        queue.append(currentnode.left)

      elif currentnode.right:
        queue.append(currentnode.right)
    
    return list

testbfs = binarysearchtree()
testbfs.insert(1)
testbfs.insert(2)
testbfs.insert(3)
testbfs.insert(6)
testbfs.insert(5)
testbfs.insert(4)

print(testbfs.breadthfirstsearch())
