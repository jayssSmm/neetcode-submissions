# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        stack = []

        while f and f.next:
            stack.append(s.val)
            s = s.next
            f = f.next.next    

        if f != None:
            s = s.next 

        while s != None:
            if stack.pop() != s.val:
                return False
            s = s.next

        return True   