# 24 OCT 2026
# Linear Queue using linked list
# Enqueue & Dequeue
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinearQueue:
    def __init__(self):
        # Header node initialized to none
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        temp = self.front
        print("deleted node: ", temp.data)
        self.front = self.front.next
        if self.front == None:   #if there's only one node
            print("Queue is empty now")
            self.rear = None
        temp = None
        

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


# create instance of class
que = LinearQueue()
# enqueue(add) some nodes
que.enqueue(Node(10))
que.enqueue(Node(20))
que.enqueue(Node(40))
que.enqueue(Node(60))
print("Linear Queue: ")
que.display()

# dequeue (delete) nodes:
print("\nafter dequeuing (first node gets deleted)")
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
