class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)



class LinkedList:
    def __int__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


    def add(self, data):
        """ Adds new Node containing data at head of the list Takes O(1) time"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


N1 = Node(10)
l1 = LinkedList()
l1.head = N1
l1.size()
print(l1.size())
