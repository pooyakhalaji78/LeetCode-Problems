# @title problem 5: Merge Two Sorted Lists
from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to simplify merging
        current = dummy  # Initialize a pointer to the dummy node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append any remaining elements from list1 or list2
        current.next = list1 if list1 else list2

        return dummy.next  # Return the merged list (excluding the dummy node)


