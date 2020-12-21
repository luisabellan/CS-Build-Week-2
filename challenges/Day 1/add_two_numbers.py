# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode():
    def __init__(self, value):
        
        if isinstance(value,int):
            self.val = value
            self.next = None
            
        elif isinstance(value,list):
            self.val = value[0]
            self.next = None
            current = self
            for i in value[1:]:
                current.next = ListNode(i)
                current = current.next
            
     
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if isinstance(l1,list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        result = head = ListNode(None)
        carry = 0
        while l1 and l2:
            quotient = l1.val + l2.val + carry // 10
            remainder = l1.val + l2.val + carry % 10
            carry = quotient
            current = remainder

            node = ListNode(current)
            head.next = node
            head, l1, l2 = head.next, l1.next, l2.next
        if l1:
            head.next = l1
        else:
            head.next = l2
       
        while carry and head.next:
            quotient = head.next.val + carry // 10
            remainder = head.next.val + carry % 10
            carry = quotient
            current = remainder
            head.next.val = current
            head = head.next
        if carry:
            head.next = ListNode(carry)

        return result.next
          
        
        
if __name__ == "__main__":
    test = Solution()
    
   
    print(test.addTwoNumbers([2,4,3],[5,6,4]))