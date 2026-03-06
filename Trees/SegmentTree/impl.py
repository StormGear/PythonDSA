class SegmentTree:
    def __init__(self, data, func=min):
        self.n = len(data)
        self.func = func # min, max or sum
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        result = float('inf') if self.func == min else float('-inf')
        while left < right:
            if left % 2:
                result = self.func(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = self.func(result, self.tree[right])
            left //= 2
            right //= 2
        return result
    
if __name__ == "__main__":
    data = [-1, 2, 4, 0]
    seg_tree = SegmentTree(data)
    
    print(seg_tree.query(0, 3))  # Output: -1
    # seg_tree.update(2, 0)
    # print(seg_tree.query(1, 5))  # Output: 0