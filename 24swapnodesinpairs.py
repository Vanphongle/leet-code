class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = head.next
        head.next, new_head.next = self.swapPairs(new_head.next), head

        return new_head
