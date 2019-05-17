class Node:
  
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 0
  def set_left(self, left):
    self.left = left
    
  def set_right(self, right):
    self.right = right
    
  def get_left(self):
    return self.left
  
  def get_right(self):
    return self.right
  
  def get_key(self):
    return self.key
  
  def set_height(self, height):
    self.height = height
  
class AVL:
  
  def __init__(self):
    self.root = None
  
  def get_root(self):
    return self.root
  
  def search(self, key):
    return self.check(self.root, key)
  
  def check(self, node, key):
    if node is None:
      return None
    
    if node.get_key() == key:
      return node
    elif node.get_key() > key:
      return self.check(node.get_left(), key)
    else:
      return self.check(node.get_right(), key)
  
  def insert(self, node):
    if self.root is None:
      self.root = node
    else:
      self.insert_node(self.root, node)

  def insert_node(self, parent, node):
    if parent.get_key == node.get_key():
      pass
    else:
      if parent.get_key() > node.get_key():
        left = parent.get_left()
        if left is None:
          parent.set_left(node)
        else:
          self.insert_node(left,node)
      else:
        right = parent.get_right()
        if right is None:
          parent.set_right(node)
        else:
          self.insert_node(right,node)

  def print_tree(self):
    self.print_node(self.root, 0)

  def print_node(self,node, depth):
    if node is not None:
      print("  "*depth + str(node.get_key()))

      self.print_node(node.get_left(), depth+1)
      self.print_node(node.get_right(), depth+1)
        
  def get_parent(self, key):
    return self.get_parent_node(self.root, key)

  def get_parent_node(self, node, key):
    if node is None:
      return None
    
    if node.get_left().get_key() == key:
      return node, 0
    elif node.get_right().get_key() == key:
      return node, 1

    elif node.get_key() > key:
      return self.get_parent_node(node.get_left(), key)
    else:
      return self.get_parent_node(node.get_right(), key)

  def delete(self, key):
    parent, locate = self.get_parent(key)
    if locate == 0:
      node = parent.get_left()
    elif locate == 1:
      node = parent.get_right()

    self.delete_node(parent, node, locate)

  def delete_node(self, parent, node, locate):
    if node.get_left() and node.get_right():
      self.twoChildDelete(parent, node, locate)
    elif node.get_left() is None and node.get_right() is None:
      self.noneChildDelete(parent,node, locate)
    else:
      self.oneChildDelete(parent, node, locate)

  def find_successor(self, parent):
    node = parent.get_left()
    child = node.get_left()
    if child is not None:
      return self.in_order(node)
    else:
      return parent, node

  def twoChildDelete(self, parent, node, locate):
    leftSubtree = node.get_left()
    rightSubtree = node.get_right()
    orderResultParent = None

    if node.get_right().get_left() == None:
      orderResult = node.get_right()
    else:
      orderResultParent, orderResult = self.in_order(node.get_right())

    if locate == 0:
      parent.set_left(orderResult)
    else:
      parent.set_right(orderResult)
    if orderResultParent:
      orderResultParent.set_left(None)
      orderResult.set_right(rightSubtree)
    orderResult.set_left(leftSubtree)


  def oneChildDelete(self, parent, node, locate):
    if node.get_left():
      if locate == 0:
        parent.set_left(node.get_left())
      else:
        parent.set_left(node.get_right())
    else:
      if locate == 0:
        parent.set_right(node.get_left())
      else:
        parent.set_right(node.get_right())

  def noneChildDelete(self, parent, node, locate):
    if locate == 0:
      parent.set_left(None)
    else:
      parent.set_right(None)

  def rocateRight(self):
    temp = self.root.get_left().get_right()
    self.root.get_left().set_right(self.root)
    self.root = self.root.get_left()
    self.root.get_right().set_left(temp)

  def rocateleft(self):
    temp = self.root.get_right().get_left()
    self.root.get_right().set_left(self.root)
    self.root = self.root.get_right()
    self.root.get_left().set_right(temp)

  def calHeight(self, node): 
    if node is None: 
      return 0 ;  
  
    else :
      lDepth = self.calHeight(node.left) 
      rDepth = self.calHeight(node.right)
      print(node.key)
      print(lDepth)
      print(rDepth)
      # if (lDepth - rDepth) >= 2:
      #   self.rocateRight()
      # elif (lDepth - rdepth) <= -2:
      #   self.rocateleft()

      if (lDepth > rDepth): 
          return lDepth+1
      else: 
          return rDepth+1


  # def checkValence(self):

bst = AVL()
node_40 = Node(40)
bst.insert(node_40)
node_15 = Node(15)
bst.insert(node_15)
node_69 = Node(69)
bst.insert(node_69)
node_54 = Node(54)
bst.insert(node_54)
node_86 = Node(86)
bst.insert(node_86)
node_50 = Node(50)
bst.insert(node_50)
node_66 = Node(66)
bst.insert(node_66)
node_83 = Node(83)
bst.insert(node_83)
node_90 = Node(90)
bst.insert(node_90)
node_99 = Node(99)
bst.insert(node_99)
result = bst.search(66)
if result is None:
  print("fail")
else:
  print("success")

result = bst.search(67)
if result is None:
  print("fail")
else:
  print("success")

print(bst.calHeight(node_40))
# bst.print_tree()