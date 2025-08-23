# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        second_head = head.next
        second = head.next

        cur = head.next.next
        second.next = None
        go_first = True
        while cur:
            # print(first)
            # print(second)
            temp = cur.next
            if go_first:
                first.next = cur
                cur.next = second_head
                first = first.next
                go_first = False
            else:
                second.next = cur
                cur.next = None
                second = second.next
                go_first = True
            cur = temp
        first.next = second_head
        return head