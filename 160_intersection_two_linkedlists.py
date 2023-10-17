class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers, one for each list
        pointerA, pointerB = headA, headB
        
        while pointerA != pointerB:
            # If either pointer reaches the end of its list, move it to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA  # Return the intersection node or None if there is no intersection
