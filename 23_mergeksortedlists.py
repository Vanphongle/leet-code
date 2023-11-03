from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        min_heap = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                min_heap.put((node.val, i, node))

        dummy = ListNode()
        current = dummy

        while not min_heap.empty():
            val, list_idx, node = min_heap.get()
            current.next = node
            current = current.next

            if node.next:
                min_heap.put((node.next.val, list_idx, node.next))

        return dummy.next
