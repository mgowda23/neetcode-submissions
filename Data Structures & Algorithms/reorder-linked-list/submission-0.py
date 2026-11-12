# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Found the middle and hence split it
        second = slow.next
        slow.next = None
        prev = None

        # Reverse the second List:
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge the 2 lists:
        first, second = head, prev # beginning of second will be prev since we reversed our second list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
            