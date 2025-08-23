# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        mid_prev = head
        mid_next = head.next.next
        cur = head.next.next

        while cur and cur.next:
            mid_prev = mid_prev.next
            mid_next = mid_next.next
            cur = cur.next.next

        mid_prev.next = mid_next
        return head