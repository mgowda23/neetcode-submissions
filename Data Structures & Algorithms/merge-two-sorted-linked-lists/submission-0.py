# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as a permanent anchor at the start.
        # This saves us from having to write messy edge-case code for the very first node.
        dummy = ListNode()

        # 'tail' is our active pointer that moves forward as we build our new merged list.
        tail = dummy

        # 2. Comparison Loop: Run as long as BOTH lists still have nodes to process.
        while list1 and list2:
            if list1.val < list2.val:
                # If list1's value is smaller, attach list1 to our merged list's tail
                tail.next = list1
                # Move list1 forward to its next node
                list1 = list1.next
            else:
                # Otherwise, attach list2 to our tail
                tail.next = list2
                # Move list2 forward to its next node
                list2 = list2.next

            # Advance the tail pointer so it's always sitting at the very end of our new list
            tail = tail.next

        # 3. Cleanup: Once the while loop ends, one list has run out of nodes.
        # Because the original lists were already sorted, whatever is left in the
        # remaining list is guaranteed to be larger than everything we've added so far.
        # We can attach the entire remainder in one single step!
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # 4. Return the result, skipping our initial dummy placeholder node.
        return dummy.next