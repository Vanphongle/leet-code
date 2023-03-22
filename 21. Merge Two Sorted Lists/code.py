class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(-1)
        
        # Create a pointer to the dummy node
        curr = dummy
        
        # Traverse both lists
        while l1 and l2:
            if l1.val <= l2.val:
                # If the current node in the first list is smaller or equal, append it to the merged list
                curr.next = l1
                l1 = l1.next
            else:
                # If the current node in the second list is smaller, append it to the merged list
                curr.next = l2
                l2 = l2.next
            
            # Move the pointer to the current node of the merged list
            curr = curr.next
        
        # Append any remaining nodes from the first or second list to the merged list
        curr.next = l1 or l2
        
        # Return the head of the merged list
        return dummy.next
