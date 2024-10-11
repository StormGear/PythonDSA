import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Problem #78 [Medium]. This problem was asked by Google.
# Merge k sorted linked lists and return it as one sorted list.
def mergeKLists(lists):
    # Custom comparison function for ListNode to be used in heap
    ListNode.__lt__ = lambda self, other: self.val < other.val
    
    # Create a min heap
    heap = []
    
    # Add the head node of each list into the heap
    for l in lists:
        if l:
            heapq.heappush(heap, l)
    
    # Create a dummy node to simplify the result list construction
    dummy = ListNode()
    current = dummy
    
    # Process the heap until it's empty
    while heap:
        # Pop the smallest node from the heap
        smallest_node = heapq.heappop(heap)
        
        # Attach the smallest node to the result list
        current.next = smallest_node
        current = current.next
        
        # If there is a next node, push it into the heap
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)
    
    # Return the merged list starting from the dummy node's next
    return dummy.next

# Helper function to convert list to linked list
def to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)) if result else "Empty List")

# Example of running a test case
lists = [
    to_linked_list([1, 4, 5]),
    to_linked_list([1, 3, 4]),
    to_linked_list([2, 6])
]

result = mergeKLists(lists)
print_linked_list(result)

