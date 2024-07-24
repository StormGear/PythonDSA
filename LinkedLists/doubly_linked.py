
# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        """
        Check if linked list is empty
        :return: If the linked list is empty (i.e., the head node is None), return True. Otherwise, 
        False.
        """
        if self.head is None:
            return True
        else:
            return False
        
    def print_LL(self):
        """
        Prints the elements of a linked list in the forward direction
        """ 
        if self.is_empty():
            print("Linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, "--->", end=" ")
                current_node = current_node.next 
                
    def print_LL_reverse(self):
        """
        Prints the elements of a linked list in reverse
        """
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node = self.head
            # navigate to the last node
            while current_node.next is not None:
                current_node = current_node.next
            # traverse backwards
            while current_node is not None:
                print(current_node.data, "--->", end=" ")
                current_node = current_node.prev
                 