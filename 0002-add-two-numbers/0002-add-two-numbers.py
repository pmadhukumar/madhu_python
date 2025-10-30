# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)   # Dummy head node to simplify result handling
        current = dummy       # Pointer to the current node in the result list
        carry = 0             # Carry for sums >= 10

        # Traverse both linked lists until both are fully processed
        while l1 or l2 or carry:
            # Get current values (0 if a list is shorter)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Create a new node with the computed digit
            current.next = ListNode(new_val)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
