queue = []

   
def enqueue():
    """
    This function adds an element to a queue.
    """
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added to queue!")
    
def dequeue():
    """
    This function removes the first element from a queue and prints the removed element.
    """
    if not queue:
        print("Queue is empty!")
    else:
        value = queue.pop(0)
        print(f"Removed element: {value}")
        
def display():
    print(queue)
    
while True:
    print("Select an operation \n1.Enqueue\n2.Dequeue\n3.Display queue \
          \n4.Quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct choice.")
    
