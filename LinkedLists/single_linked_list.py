# add, traversal and deletion operation 
# Define the node as a class 


class Node:
    '''  Create a Node for a singly linked list '''
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self) -> None:
        """ Create a linked list """
        # The head is used for traversal, typically points to the first node
        self.head = None
        
    def data_at_head(self):
        """
        Prints the data present at the node the head is currently pointing to
        """
        print(f"Data at the head is {self.head.data}")
        
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
        
    # Define methods that perform operations
    def print_LI(self):
        '''
        Print the data of each node in a linked list.
        '''
        if self.head is None:
            print("Linked List is empty!")
        else:
            current_node = self.head
            # while head is not empty print the data
            while current_node:
                print(current_node.data, "--->", end=" ")
                # go to the next node
                current_node = current_node.next
            print("None")
     
    def insert_empty(self, data):
        """
        Add a new node to an empty linked list.
        :param data: The data stored in the new node
        """
        if self.is_empty():
             new_node = Node(data)
             self.head = new_node
        else:
            print("Linked list is not empty")
             
    def add_begin(self, data):
        """
        Adds a new node to the beginning of a linked list.
        :param data: The data stored in the new node
        """
        new_node = Node(data)
        # change reference of the new node
        new_node.next = self.head
        # set the head pointer to the new node
        self.head = new_node
        
    def add_end(self, data):
        """
        Adds a new node to the end of a linked list.
        :param data: The data stored in the new node
        """
        new_node = Node(data)
        # check if the linked list is empty
        # if it is the new node becomes the first node
        if self.is_empty():
            self.head = new_node
        else:
            # traverse to the last node and add the new node
            current_node = self.head
            # where the is another node after the current node
            while current_node.next is not None:
                # update the current node to the next
                current_node = current_node.next
            # Modify reference of the second to last node to that of the new node
            current_node.next = new_node
            
    def after_node(self, data, x):
        """
        Add a new node after a specified node in a linked list.
        :param data: The data to be stored in the new node 
        :param x: x is the data value of the node after which the new node needs to be inserted.
        """
        current_node = self.head
        while current_node is not None:
            # stop traversal upon finding the element
            if x == current_node.data:
                break
            current_node = current_node.next
        if current_node is None:
            print("Specified node is not present.")
        else:
            new_node = Node(data)
            # assign the reference of current_node to the new node
            new_node.next = current_node.next
            # assign the new_node as the ref of the current_node
            current_node.next = new_node  
            
    def add_before(self, data, x):
        """
        Add a new node before a specified node in a linked list.
        :param data: The data to be stored in the new node 
        :param x: x is the data value of the node before which the new node needs to be inserted.
        """
        # first check if the linked list has content
        if self.is_empty():
            print("Linked List is empty!")
            return
        
        # first check if the new node is being added before the first node
        if self.head.data == x:
            self.add_begin(data)
            return
            
        # if it is within the linked list
        current_node = self.head
        while current_node is not None:
            if current_node.next.data == x:
                # first locate the previous node before the specified node
                prev_node = current_node
                # insert a new node after the previous node
                self.after_node(data, prev_node.data)
                return
            
                # Alternative implementation
                # new_node = Node(data)
                # new_node.next = current_node.next
                # current_node.next = new_node
                # return
            current_node = current_node.next 
    
    def delete_begin(self):
        """
        Deletes the first node of a linked list if it exists, otherwise it prints an error
        message.
        """
        # check if deletion is possible
        if self.is_empty():
            print("Deletion failed, empty linked list.")  
        else:
            self.head = self.head.next
            
    def delete_end(self):
        """
        Delete the last node of a linked list if it exists, otherwise it prints an error
        message.
        """
        # check if deletion is possible
        if self.is_empty():
            print("Deletion failed, empty linked list.")
        # or if the LL contains just one node
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            # while the ref of the nexxt node after the current node is not None, it means we are not at the end
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None

    def reverse_LL(self, head):
        """
        Reverse a linked list
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
            
    def delete_by_value(self, x):
        """
        Delete a node provided the value of the node is known
        """
        if self.is_empty():
            print("Deletion failed, empty linked list.")
            return
        # if specified node is the first node
        if self.head.data == x:
            self.delete_begin()
            return
        # if it is within the linked list
        # find the previous node of the given node
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == x:
                prev_node = current_node
                break
            current_node = current_node.next
        if current_node.next is None:
            print("Specified node not present!")
        else:
            prev_node.next = prev_node.next.next
            
            
            
             
        
            
        
        
                
                
LL1 = Linked_list()
LL1.add_begin(10)
LL1.add_end(20)
LL1.add_end(30)
LL1.add_end(40)
LL1.print_LI()
print("Reversed Linked List")
LL1.head = LL1.reverse_LL(LL1.head)
LL1.print_LI()
# LL1.add_begin(20)
# LL1.add_begin(30)
# LL1.add_end(30)
# LL1.add_end(50)
# LL1.add_before(25, 30)
# LL1.add_before(35, 50)
# LL1.add_before(28, 30)
# LL1.insert_empty(20)
# LL1.delete_begin()
# LL1.delete_end()
# LL1.delete_end()

# LL1.delete_by_value(50)
# LL1.print_LI()

             
            
            
            
             
         