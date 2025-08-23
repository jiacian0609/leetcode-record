# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []

        slow = head
        fast = head

        while fast and fast.next:
            nums.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        print(nums)

        max_sum = 0
        idx = len(nums) - 1
        while slow:
            cur_sum = nums[idx] + slow.val
            max_sum = max(max_sum, cur_sum)
            slow = slow.next
            idx -= 1
        return max_sum