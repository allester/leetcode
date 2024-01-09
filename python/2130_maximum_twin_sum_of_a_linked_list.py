'''
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/submissions/1141797632/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find midpoint
        s = head
        f = head
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
        prev.next = None

        #reverse starting at midpoint
        prev = None
        curr = s
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #add values together
        ans = 0
        head2 = prev
        head1 = head
        while head1 and head2:
            ans = max(ans, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next

        return ans