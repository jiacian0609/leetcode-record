# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next      # 暫存下一個節點
            cur.next = prev      # 反轉指向
            prev = cur           # prev 往前移
            cur = temp           # cur 往前移
        
        return prev  # prev 最後會是新的 head
