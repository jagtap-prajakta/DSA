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

    def sum_consecutive(self):
        if self.head == None or self.head.next == None:
            print("List should contain atleast 2 nodes")
            return
        temp = self.head

        while temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next   


list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
# list.append(Node(40))

print("Linked List: ")
list.display()
print("Sum of 2 consecutive nodes")
list.sum_consecutive()