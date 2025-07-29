class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search_list(self, data):
        current = self.head
        isfound = False
        counter = 1
        while current:
            if(data == current.data):
                print(data, "found on position", counter)
                isfound = True
            current = current.next
            counter += 1
        if not isfound:
            print(data, "not found in the list")

    def delete_list(self, data):
        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        prev.next = current.next

        
l1 = LinkedList()
l1.insert_at_end(3)
l1.insert_at_begining(1)
l1.insert_at_begining(2)
l1.insert_at_begining(4)
l1.insert_at_end(5)
l1.print_list()
l1.search_list(3)
l1.delete_list(2)
l1.print_list()