'''
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/1141778444/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        s = head
        f = head.next.next

        while f and f.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        
        return head