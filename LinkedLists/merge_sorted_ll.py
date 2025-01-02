class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merged_sorted_ll(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next
    
if __name__ == '__main__':
    soln = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    result = soln.merged_sorted_ll(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next