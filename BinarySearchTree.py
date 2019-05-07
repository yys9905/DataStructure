class Node:
  
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    
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
  
class Binary_search_tree:
  
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

  def in_order(self, parent):
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

bst = Binary_search_tree()
node_40 = Node(40)
bst.insert(node_40)
node_15 = Node(15)
bst.insert(node_15)
node_69 = Node(69)
bst.insert(node_69)
node_8 = Node(8)
bst.insert(node_8)
node_25 = Node(25)
bst.insert(node_25)
node_54 = Node(54)
bst.insert(node_54)
node_86 = Node(86)
bst.insert(node_86)
node_5 = Node(5)
bst.insert(node_5)
node_10 = Node(10)
bst.insert(node_10)
node_20 = Node(20)
bst.insert(node_20)
node_30 = Node(30)
bst.insert(node_30)
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

bst.print_tree()
bst.delete(86)
bst.print_tree()