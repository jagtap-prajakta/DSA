# 08 Oct 2026:
# Deleting node in a Singly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next  
            temp.next = new_node #appending new_node

    #   Reversing a SLL
    def reverse_list(self):
        current = self.head
        prev = None
        while (current):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

            

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(-35)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(40))

print("Linked List: ")
list.display()

print("After reversing: ")
list.reverse_list()
list.display()