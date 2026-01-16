
class SortingAlgorithms:
    # Time: O(n^2)
    # Space: O(1)
    # compare adjacent elements and swap them
    def bubble_sort(self, arr):
        n = len(arr) 
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, n-1):
                if arr[i] > arr[i+1]:
                    sorted = False
                    arr[i], arr[i+1] = arr[i+1], arr[i]

    # Time: O(n^2)
    # Space: O(1)
    # maintain a sorted and unsorted portion, by continuosly swapping to maintain sorted part
    def insertion_sort(self,arr):
        n = len(arr)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j-1] > arr[j]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                else:
                    break
    # Time: O(n^2)
    # Space: O(1)
    # sorted and unsorted portions, look for min in unsorted portion and swap
    def selection_sort(self,arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Time: O(nlogn)
    # Space: O(n)
    # keep dividing until a single element, recursively
    def merge_sort(self, arr):
        n = len(arr) 

        if n <= 1:
            return arr
        
        m = n // 2
        L = arr[:m]
        R = arr[m:]

        L, R = self.merge_sort(L), self.merge_sort(R)
        l, llen, r, rlen = 0, len(L), 0, len(R)

        sorted_arr = [0] * n
        i = 0

        while l < llen and r < rlen:
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
            i += 1

        while l < llen:
            sorted_arr[i] = L[l]
            l += 1
            i += 1

        while r < rlen:
            sorted_arr[i] = R[r]
            r += 1
            i += 1

        return sorted_arr
    
    # Time: avg: O(nlogn) worst: O(n^2) if you keep choosing a bad pivot
    # Space: O(n)
    # Find a pivot and elements to the right and left of it
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        p = arr[-1]

        # L = [x for x in arr[:-1] if x <= p]
        L = list(filter(lambda x: x <= p, arr[:-1]))
        R = list(filter(lambda x: x > p, arr[:-1]))
        # R = [x for x in arr[:-1] if x > p]

        L = self.quick_sort(L)
        R = self.quick_sort(R)

        return L + [p] + R
    
    # Time: O(k + n), k is the max in the input arr
    # Space O(k), for the counts arr
    # Use a counts arr, having index of the arr as the count of each element
    def counting_sort(self, arr):
        maxx = max(arr)
        counts = [0 for _ in range(maxx+1)]

        for num in arr:
            counts[num] += 1

        i = 0
        for c in range(maxx+1):
            while counts[c]:
                arr[i] = c
                i += 1
                counts[c] -= 1

    def heapify(self, arr, n, i): # n: length of array, i: the index of the node we want to fix
        """Ensure subtree with root i is a max-heap."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # is left child greater
        if left < n and arr[left] > arr[largest]:
            largest = left

        # is right child greater
        if right < n and arr[right] > arr[largest]:
            largest = right

        # if largest is not root, swap (i.e it has violated the heap property) and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        # build a max heap starting at the first non-leaf node(i.e fix all non-leaf nodes)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i) # fix all non-leaf nodes

        # extract elements one by one
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0] # heap property may be violated after arr[0] = arr[i]

            # heapify reduced heap
            self.heapify(arr, i, 0)

        return arr






if __name__=="__main__":
    soln = SortingAlgorithms()
    A = [-5,3,2,1,-3,-3,7,2,2]
    B = [5,3,2,1,3,3,7,2,2]
    C = [12,11,13,5,6,7]
    # soln.bubble_sort(A)
    # soln.insertion_sort(A)
    # soln.selection_sort(A)
    # print(soln.merge_sort(A))
    # print(soln.quick_sort(B))
    # soln.counting_sort(B)
    print(soln.heap_sort(C))
    # print(B)