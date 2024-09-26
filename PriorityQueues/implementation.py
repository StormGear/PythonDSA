from queue import PriorityQueue
import heapq
# implementing a Priority Queue using a list
class PriorityQueue1:
    """
    Priority Queue implementation using a list where the least valued element is removed first or least valued element has the highest priority
    """
    def __init__(self):
        self.queue = list()

    def insert_element(self, data):
        self.queue.append(data)

    def show(self):
        self.queue.sort()
        print(self.queue)

    def delete(self):
        self.queue.sort()
        self.queue.pop(0)

class PriorityQueue2:
    """
    Priority Queue implementation using a list where the most valued element is removed first or most valued element has the highest priority
    """
    def __init__(self):
        self.queue = list()

    def insert_element(self, data):
        self.queue.append(data)

    def show(self):
        self.queue.sort(reverse=True)
        print(self.queue)

    def delete(self):
        self.queue.sort(reverse=True)
        self.queue.pop(0)

class PriorityQueue3:
    """
    Priority Queue implementation using the queue module
    """
    def __init__(self):
        self.queue = PriorityQueue()

    def insert_element(self, data):
        self.queue.put(data)

    def show(self):
        print(list(self.queue.queue))
    
    def delete(self):
        self.queue.get()

class PriorityQueue4:
    """ 
    PQ implementation using tuples as elements, such that the first element of the tuple is the priority and the second element is the data
    (priority, data)
    """
    def __init__(self):
        self.queue = list()

    def insert_element(self, data):
        self.queue.append(data)

    def show(self):
        # reverse the sort order to achieve the reverse of the priority queue
        self.queue.sort()
        print(self.queue)
    
    def delete(self):
        self.queue.pop(0)

class PriorityQueue5():
    """
    PQ implementation of a min heap using binary heap provided by the heapq Python module
    """
    def __init__(self) -> None:
        self.heap = list()

    def insert_element(self, data):
        heapq.heappush(self.heap, data)

    def show(self):
        print(self.heap)

    def delete(self):
        heapq.heappop(self.heap)
        
    

if __name__ == '__main__':
    # create a Priority Queue object
    pq = PriorityQueue1()
    pq = PriorityQueue2()
    pq = PriorityQueue3()
    pq = PriorityQueue4()
    pq = PriorityQueue5()
    # insert data
    pq.insert_element(1)
    pq.insert_element(2)
    pq.insert_element(0)
    pq.show()
    pq.delete()
    pq.delete()
    print("After deleting an element")
    pq.show()