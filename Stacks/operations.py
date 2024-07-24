stack = []

def push():
    """
    This function pushes an element onto a stack if it is not already full.
    """
    if len(stack) == stack_size: 
        print("Stack is already full!\n")
        return
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)
    
def pop_element():
    """
    This function removes the top element from a stack and prints the removed element and the updated
    stack.
    """
    if not stack:
        print("Stack is empty!\n")    
    else:
        value = stack.pop()
        print(f"Removed element: {value}\n")
        print(stack)
        
def peek():
    """
    The function "peek" prints the element at the top of a stack.
    """
    top = stack[-1]
    print(f"The element at the top: {top}")
    
def is_empty():
    """
    The function checks if a stack is empty and returns True if it is.
    :return: a boolean value of True if the stack is empty, and False if it is not empty.
    """
    if not stack:
        return True
    else:
        return False
    
    
stack_size =  int(input("Enter the size of the stack: "))   
while True:
    print("Select the operation to perform: \
          \n1.Push\n2.Pop\n3.Peek\n4.Is stack empty?\n5.Quit\nEnter your choice: ") 
    choice = int(input())
    
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        peek()
    elif choice == 4:
        if is_empty():
            print("Stack is empty\n")
        else:
            print("Stack is not empty\n")
    else:
        print("Select the right operation")
        
        
        