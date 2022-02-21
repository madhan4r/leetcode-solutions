# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rNode = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            a3 = int(a1) + int(a2) + carry
            carry = a3//10
            a3 = a3 % 10
            dummy.val = a3
            if l1 or l2 or carry:
                dummy.next = ListNode()
                dummy = dummy.next
        return rNode