# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        mid = head.next
        cur = head.next.next
        while cur and cur.next:
            mid = mid.next
            cur = cur.next.next
        return mid