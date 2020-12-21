# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node


class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        output1 = [i.val for i in list1]
        output2 = [i.val for i in list2]
        # print(output2)
        output3 =  []
        output3 += output1 + output2
        print(output3)
        return output3
        

list1 = ListNode()
list1.add(Node(1))
list1.add(Node(2))
list1.add(Node(4))

list2 = ListNode()
list2.add(Node(1))
list2.add(Node(3))
list2.add(Node(4))


Solution().mergeTwoLists(list1,list2)