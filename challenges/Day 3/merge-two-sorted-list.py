# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class ListNode():
    def __init__(self, value):
        
        if isinstance(value,int):
            self.val = value
            self.next = None
            
        elif isinstance(value,list):
            self.val = value[0]
            self.next = None
            cur = self
            for i in value[1:]:
                cur.next = ListNode(i)
                cur = cur.next




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if isinstance(l1,list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)
        
        prev = dummy = ListNode(None)

        while l1 and l2:
            
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
        prev = prev.next
        prev.next = l1 or l2
        print(dummy.next)
        return dummy.next


        

list1 = ListNode([1,2,4])
list2 = ListNode([1,3,4])



Solution().mergeTwoLists(list1,list2)