# 07 Oct 2026:
# Inserting node at any position in SLL

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

    # Insertion operations : 
    def insert(self, new_node, pos):
        temp = self.head 
        if pos == 1:   #inserting at first position
            new_node.next = self.head
            self.head = new_node
        else:  #inserting node from 2nd to last position
            p = 1
            # temp = self.head
            while(p != pos-1 and temp.next != None):  # or condition to prevent if user enter invalid node position
                temp = temp.next
                p += 1 
            new_node.next = temp.next
            temp.next = new_node


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
list.display()
print("Inserting node at first position")
list.insert(Node(100), 1)
list.display()
print("Inserting node in between (at position 4): ")
list.insert(Node(66), 4)
list.display()
list.insert(Node(90), 8)
list.display()