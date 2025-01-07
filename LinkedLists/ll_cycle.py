# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: list[ListNode]) -> bool:
        # index = 0
        seen = set()

        while head:
            if head.val in seen:
                return True
            seen.add(head.val)
            head = head.next

        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        index = 0
        seen = []

        while head:
            if head in seen:
                index = seen.index(head) + 1
                print(index)
                return True
            seen.append(head)
            head = head.next

        index = -1
        print(index)
        return False
    
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    
if __name__ == '__main__':
    soln = Solution()
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    print(soln.hasCycle(l1))