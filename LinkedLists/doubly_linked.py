
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
        Check if linked list is empty \n
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
            print("None")
                
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
            print("None")
    
    def insert_empty(self, data) -> None:
        """
        Inserts a new node at the beginning of the doubly linked list. \n
        :param data: The data to be stored in the new node
        """
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
        else:
            print("Doubly linked list is not empty")
            
    def insert_begin(self, data) -> None:
        """
        Inserts a new node at the beginning of the doubly linked list. \n
        :param data: The data to be stored in the new node
        """
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_end(self, data) -> None:
        """Insert a node at the end of the doubly linked list

        Parameters:
            data: data to be stored in the node
        """
        if self.is_empty():
            self.insert_empty(data)
        else:
            current_node = self.head
            new_node = Node(data)
            # navigate to the last node
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            
    def insert_after(self, data, x):
        """Insert a node after a given node
        
        Parameters:
            data: data to be added to the new node
            x: data of the node after which the new node will be inserted
        """
        if self.is_empty():
            print("Doubly linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == x:
                    break
                current_node = current_node.next
            if current_node is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = current_node.next
                new_node.prev = current_node 
                if current_node.next is not None:
                    current_node.next.prev = new_node
                current_node.next = new_node
                
    def insert_before(self, data, x):
        """Insert a node before a given node
        
        Parameters:
            data: data to be added to the new node
            x: data of the node before which the new node will be inserted
        """
        if  self.is_empty():
            print("Doubly linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == x:
                    break
                current_node = current_node.next
            if current_node is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = current_node
                new_node.prev = current_node.prev
                # adding the node within the linked list
                if current_node.prev is not None:
                    current_node.prev.next = new_node
                # adding the node before the first node
                else:
                    self.head = new_node
                current_node.prev = new_node
                

                
            
                    
                
                
            
                

    
if __name__ == '__main__':
    dll = DoublyLL()
    # dll.insert_empty(10)
    dll.insert_begin(50)
    dll.insert_begin(40)
    dll.insert_begin(30)
    dll.insert_begin(20)
    dll.insert_begin(10)
    dll.insert_after(60, 50)
    dll.insert_after(15, 10)
    dll.insert_before(9, 10)
    dll.print_LL()
    # dll.print_LL_reverse()
                 