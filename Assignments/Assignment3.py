# Hospital Emergency Management using Priority Queue

# Create a node to store the details of one patient
class Node:
    def __init__(self, pid, name, pr):
        self.id = pid
        self.name = name
        self.priority = pr
        self.next = None

# priority queue class
class PriorityQueue:
    def __init__(self):
        # intially front and rear are empty
        self.front = self.rear = None

    # 1. add patient (enqueue)
    def enqueue(self, new_node):
        # if queue is empty
        if self.front == None:
            self.front = self.rear = new_node  #if no patient is present, the new patient becomes both front and rear
            return

        # if new patient has higher priority
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return
        
        # find the correct position for the new patient
        temp = self.front
        while temp.next:
            if new_node.priority < temp.next.priority:
                break
            temp = temp.next

        # insert the new patient at the correct position
        new_node.next = temp.next
        temp.next = new_node
        # update rear if patient is added at the end
        if new_node.next == None:
            self.rear = new_node

    # 2. Display the next patient to be treated. (display_next)
    def display_next(self):
        if self.front == None:
            print("No patients waiting")
        else:
            print("Next patient to be treated: ")
            print("Patient ID:", self.front.id)
            print("Patient Name:", self.front.name)
            print("Priority: ", self.front.priority)

    # 3. Remove a patient from the queue after treatment. (dequeue) 
    def dequeue(self):
        if self.front == None:
            print("No patients to remove")
        else:
            temp = self.front
            print("Patient treated: ", temp.name)

            # move front to the next patient
            self.front = self.front.next

            # if queue becomes empty update rear also
            if self.front == None:
                self.rear = None

    # 4. Display all waiting patients in priority order(display_all)
    def display_all(self):
        if self.front == None:
            print("No patients waiting")
        else:
            temp = self.front
            print("\n Waiting Patients:")
            while temp:
                print("ID:", temp.id,
                      "Name: ", temp.name,
                      "Priority: ", temp.priority)
                temp = temp.next


# Create priority queue
pq = PriorityQueue()
# Main menu
while True:
    print("\n --- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display next patient")
    print("3. Remove Pateient")
    print("4. Display all patients")
    print("Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient name: ")
        pr = int(input("Enter priority (1-Critical, 2-Serious, 3-Normal):"))

        # create a new patient node
        new_node = Node(pid, name, pr)

        # add patient to priority queue
        pq.enqueue(new_node)
        print("Patient Added successfully!")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")