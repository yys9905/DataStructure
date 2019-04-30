class Node:
  
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
        
    def get_prev(self):
        return self.prev

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class doubly_linked_list:

    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.size += 1
        if self.header is None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
        self.tail = new_node
        
    def print_list(self):
        print(">> current list")
        node = self.header
        while node is not None:
            print(node.get_data())
            node = node.get_next()
        print(">>>>>>>>>>>>>>>>")

    def get_at(self, index):
        if index >= self.size:
            return None
        else:
            node = self.header      
            for i in range (0, index):
                node = node.get_next()
            return node
    
    def search(self, data):
        node = self.header
        while node is not None:
            if node.get_data() == data:
                return node
            node = node.get_next()
        return node

dll = doubly_linked_list()
dll.append("Apple")
dll.append("Kiwi")
dll.append("Banana")
dll.print_list()