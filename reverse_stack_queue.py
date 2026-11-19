# 18 NOV 2026
# REVSERSE STACK QUEUE

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
        def __init__(self):
            self.top= None
        def isempty(self):
            return self.top is None
        
        def push(self,newnode):
            newnode.next = self.top
            self.top = newnode

        def pop(self):
             temp=self.top
             if self.isempty():
                print("Stack is Empty")

             else:
                #  print("\nPoped Element: ",temp.data)
                #  self.top=self.top.next
                #  temp=None
                temp = self.top
                popped_data = temp.data
                self.top = self.top.next
                temp = None
                return popped_data

            

        def print(self):
            if self.isempty():
                print("Stack is Empty\n")
            else:
                print("Stack contains....")
                temp = self.top
                while temp :
                    print(temp.data)
                    temp=temp.next


class linearQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None 
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear=newnode

        else:
            self.front =self.rear=newnode
    def dequeue(self):

        temp = self.front
        deued_data = temp.data
        self.front=self.front.next

        if self.front == None:# if there only one node
            print("Queue is Emplty Now...")
            self.rear = None

        temp = None
        return deued_data
    def print(self):
        temp = self.front 
        while temp :
            print(temp.data,end  = "->")
            temp= temp.next
        print(None)



def reverse_stack(s1):

    #reversing stack using q
    #print("Reversed Stack")
    q1 = linearQueue()
    while not s1.isempty(): # pop from stack and enqueue to queue
        q1.enqueue(Node(s1.pop())) 
    #q1.print()


    while not q1.isempty():
        s1.push(Node(q1.dequeue()))

    s1.print()


Q = linearQueue()
Q.enqueue(Node(230))
Q.enqueue(Node(400))
Q.enqueue(Node(223))
Q.enqueue(Node(132))
Q.enqueue(Node(231))

Q.print()


st=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()

reverse_stack(st)