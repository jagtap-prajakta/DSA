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

    def delete(self, value):
        temp = self.head
        prev = None
        # deleting first node
        if temp.data == value:    #searching value
            self.head = self.head.next
            return
        while (temp):
            if temp.data == value:
                break
            else:    #traverse
                prev = temp
                temp = temp.next
        if temp == None:
            print("Node value is not present in the list")
            return
        prev.next = temp.next
        temp = None

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

list.delete(40)
print("After deleteing first value: ")
list.display()