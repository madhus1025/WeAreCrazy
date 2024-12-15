'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def goTillN(self, head, n) -> Optional[ListNode]:
        cur = head
        while (n):
            cur = cur.next
            n-=1
        
        return cur

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point1, point2, prev = head, self.goTillN(head, n), None

        while point2:
            prev = point1
            point1 = point1.next
            point2 = point2.next
        
        if prev:
            prev.next = point1.next
            return head
        else:
            return head.next
        