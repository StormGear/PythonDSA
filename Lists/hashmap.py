class ListNode:
    def __init(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(10**4)]

    def hash(self, key: int) -> int:
        return key % 10**4
        

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
            cur = cur.next
        cur.next = ListNode(key, value)   

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur:
            if cur.next.key == key:
                cur = cur.next.next
                return
            cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
param_2 = obj.get(1)
obj.remove(1)