'''
https://leetcode.com/problems/merge-two-sorted-lists/submissions/983279156/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr, list1 = curr.next, list1.next
            else:
                curr.next = list2
                curr, list2 = curr.next, list2.next

        if list1 or list2:
            curr.next = list1 if list1 else list2
        
        return head.next