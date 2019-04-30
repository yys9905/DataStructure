class Node:
    def __init__(self, fruit):
        self.fruit = fruit
        self.next = None

    def get_fruit(self):
        return self.fruit

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class Simply_linked_list:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def append(self, fruit):
        new_node = Node(fruit)
        self.size += 1
        if self.header is None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node

    def get_at(self, index):
        if index >= self.size:
            return None
        else:
            node = self.header
            for i in range(index):
                node = node.get_next()
            return node

    def search(self, fruit):
        node = self.header
        while node is not None:
            if node.get_fruit() == fruit:
                return node
            node = node.get_next()
        return None
    
    def print_list(self):
        print(">>current list")
        node = self.header
        while node is not None:
            print(node.get_fruit())
            node = node.get_next()
        print(">>>>>>>>>>>>>>")

sll = Simply_linked_list()
sll.append("Apple")
sll.append("Kiwi")
sll.append("Banana")
sll.print_list()

node = sll.get_at(1)
if node is not None:
    print(node.get_fruit())
else:
    print("index error")

node = sll.get_at(2)
if node is not None:
    print(node.get_fruit())
else:
    print("index error")


node = sll.search("Banana")
if node is not None:
    print("We have it!")
else:
    print("We don't have it!")