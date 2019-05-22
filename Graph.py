class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
    self.visited = False
    
  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def set_visited(self, visited):
    self.visited = visited

  def get_data(self):
    return self.data

  def get_neighbors(self):
    return self.neighbors

  def get_visited(self):
    return self.visited


class Graph:
  def __init__(self):
    self.nodes = []

  def add_node(self, node):
    self.nodes.append(node)

  def bfs(self):
    self.__dir__breadth_first_search(self.nodes[0])

  def breadth_first_search(self, node):
    queue = []
    queue.append(node)
    node.set_visited(True)
    while(queue == []):
      if node.get_neighbors() is None:
        node = queue.pop(0)
      else:
        queue.append(node.get_neighbors()[0])
        
      







    

graph = Graph()

node_A = Node('A')
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_S = Node('S')
graph.add_node(node_S)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_S)

node_B.add_neighbor(node_A)

node_C.add_neighbor(node_D)
node_C.add_neighbor(node_E)
node_C.add_neighbor(node_F)
node_C.add_neighbor(node_G)
node_C.add_neighbor(node_S)

node_D.add_neighbor(node_C)

node_E.add_neighbor(node_C)
node_E.add_neighbor(node_H)

node_F.add_neighbor(node_C)
node_F.add_neighbor(node_G)

node_G.add_neighbor(node_F)
node_G.add_neighbor(node_S)

node_H.add_neighbor(node_E)
node_H.add_neighbor(node_G)

node_S.add_neighbor(node_A)
node_S.add_neighbor(node_C)
node_S.add_neighbor(node_G)

print("[BFS result]")
graph.bfs()
