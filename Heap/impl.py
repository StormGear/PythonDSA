# max heap implementation 
# min heap implementation
CAPACITY = 10

class MaxHeap:
    def __init__(self):
        self.heap = [0] * CAPACITY
        # actual number of elements in the heap
        self.heap_size = 0

    def insert(self, item):
        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap property/heap invariant
        self.fix_up(self.heap_size - 1)

    # time complexity: O(logN)
    def fix_up(self, index):
        parent_index = (index - 1) // 2

        # while the index > 0 means we are not at the root of the heap
        # and the item is greater than the parent, heap property is violated
        # so we need to fix it by swapping the item with the parent
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        return self.heap[0]
    
    # return and removes the root node
    def poll(self):
        max_item = self.get_max()

        # swap the root with the last element in the heap
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1

        # fix down the root element an operation called heapify
        self.bubble_down(0)

        return max_item
    
    # Since we are removing the root element, we need to fix the heap property
    # Starting from the root node, we compare the root node with its children
    # and swap the root node with the largest child 
    # time complexity: O(logN)
    def bubble_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        index_largest = index

        # compare with left child
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left

        # compare with right child
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right

        # if the index is not the largest, swap with the largest child
        # if the parent is not the largest, swap with the largest child
        # terminate if the parent is the largest
        if index != index_largest:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.bubble_down(index_largest)

    def heap_sort(self):
        # swap the root with the last element in the heap
        for i in range(self.heap_size):
            max_item = self.poll()
            print(max_item)


class MinHeap:
    def __init__(self):
        self.heap = [0] * CAPACITY
        # actual number of elements in the heap
        self.heap_size = 0

    def insert(self, item):
        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap property/heap invariant
        self.bubble_up(self.heap_size - 1)

    # time complexity: O(logN)
    def bubble_up(self, index):
        parent_index = (index - 1) // 2

        # while the index > 0 means we are not at the root of the heap
        # and the item is greater than the parent, heap property is violated
        # so we need to fix it by swapping the item with the parent
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.bubble_up(parent_index)

    def get_min(self):
        return self.heap[0]
    
    # removes and returns the root node
    def poll(self):
        max_item = self.get_min()

        # swap the root with the last element in the heap
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        self.heap_size -= 1

        # fix down the root element an operation called heapify
        self.bubble_down(0)

        return max_item
    
    # Since we are removing the root element, we need to fix the heap property
    # Starting from the root node, we compare the root node with its children
    # and swap the root node with the largest child 
    # time complexity: O(logN)
    def bubble_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        index_largest = index

        # compare with left child
        if index_left < self.heap_size and self.heap[index_left] < self.heap[index]:
            index_largest = index_left

        # compare with right child
        if index_right < self.heap_size and self.heap[index_right] < self.heap[index_largest]:
            index_largest = index_right

        # if the index is not the largest, swap with the largest child
        # if the parent is not the largest, swap with the largest child
        # terminate if the parent is the largest
        if index != index_largest:
            self.heap[index], self.heap[index_largest] = self.heap[index_largest], self.heap[index]
            self.bubble_down(index_largest)

    def heap_sort(self):
        # swap the root with the last element in the heap
        for i in range(self.heap_size):
            max_item = self.poll()
            print(max_item)

if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(8)
    min_heap.insert(12)
    min_heap.insert(20)
    min_heap.insert(-2)
    min_heap.insert(0)
    min_heap.insert(1)

    # heap.heap_sort()
    min_heap.heap_sort()