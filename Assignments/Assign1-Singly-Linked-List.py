class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    # create linked list
    def __init__(self):
        self.head = None

    # traverse and print the node values
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head 
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    # # insert node at specific position
    # def insert(self, new_node, pos):
    #     temp = self.head  #points to first node
    #     if pos == 1:
    #         new_node.next = self.head
    #         self.head = new_node
    #     else:    #inserting node from 2nd to last node
    #         for i in range(1, pos - 1):  
    #             temp = temp.next
    #         new_node.next = temp.next  # connects the new_node to the next node 
    #         temp.next = new_node    #connect the previous node to the new_node

    # # find middle node and print its value
    # def middle(self):
    #     temp1 = self.head
    #     temp2 = self.head

    #     while temp2 and temp2.next:
    #         temp1 = temp1.next
    #         temp2 = temp2.next.next
    #     print(temp1.data)

    # # delete node
    # def delete(self, value):
    #     # initialize variables
    #     temp = self.head    #temp points to the current node
    #     prev = None    #prev stores the previous node

    #     # search for the value while loop searches for the node containing the value
    #     while temp:
    #         if temp.data == value:
    #             # delete the node
    #             if prev == None:    #first node is being deleted
    #                 self.head = temp.next
    #             else:    #otherwise, connect the previous node to the next node, skipping the node being deleted
    #                 prev.next = temp.next
    #             return
    #         # move to the next node : if the value is not found these statements mode through the list until the end
    #         prev = temp 
    #         temp = temp.next 
    #     print("Value not found")

    # # REVERSE THE LIST:
    # def reverse(self):
    #     current = self.head
    #     prev = None
    #     while current:
    #         nextNode = current.next
    #         current.next = prev
    #         prev = current
    #         current = nextNode
    #     self.head = prev

    # # Calculate the sum of every two consecutive values
    # def sum_consecutive(self):
    #         if self.head == None or self.head.next == None:
    #             print("List should contain atleast 2 nodes")
    #             return
    #         temp = self.head
    
    #         while temp.next:
    #             print(temp.data + temp.next.data)
    #             temp = temp.next

    # displaying list
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
list.append(Node(50))
print("LinkedList")
list.display()

print("Insert at first position")
list.insert(Node(5),1)
list.display()

print("Insert at any other position")
list.insert(Node(15), 3)
list.display()

print("Middle Node")
list.middle()

print("Delete value: after deleting")
list.delete(5)
list.display()

# print("after Reversing the list")
# list.reverse()
# list.display()

print("Sum of 2 consecutive nodes in the list")
list.sum_consecutive()