'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
class Solution:
    def recurNodes(self, head, prev, target):
        if not head:
            return 0
        
        # Recursively find the position of the current node from the end
        pos = 1 + self.recurNodes(head.next, head, target)
        
        # If the position matches the target, remove the node
        if pos == target:
            if prev:  # If there's a previous node, skip the current node
                prev.next = head.next
            else:  # If there's no previous node, we are removing the head
                self.new_head = head.next  # Update the new head of the list
        
        return pos

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.new_head = head  # Initialize the new head to the original head
        self.recurNodes(head, None, n)
        return self.new_head
