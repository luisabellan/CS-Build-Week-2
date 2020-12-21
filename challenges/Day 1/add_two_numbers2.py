# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class SinglyLinkedList:
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.l1 = l1
        self.l2 = l2
        # sum digits in first number
        first_list = []
        second_list = []
        first_list += [node.val for node in self.l1]
        second_list += [node.val for node in self.l2]
        

        # print([n.val for n in list1 ])
        print(first_list)
        print(second_list)

        # get first number
      
        first_list = [n for n in reversed(first_list)]
       
        # print(first_list)
       
        factor = 0
        first_number = 0
        for i in range(len(first_list)):
            first_number += first_list[i] * 10 ** (factor+i)
        print(first_number)



        # get second number
      
        second_list = [n for n in reversed(second_list)]
       
        # print(second_list)
       
        factor = 0
        second_number = 0
        for i in range(len(second_list)):
            second_number += second_list[i] * 10 ** (factor+i)
        # print(second_number)

        # add numbers
        sum = first_number + second_number
        # print(sum)

        # convert sum into linked list in reversed order
        sum_str = reversed(str(sum))
        
        sum_array = []
        sum_array += [int(i) for i in sum_str]
        # print(sum_array)

        
        # create linked list as the answer
        answer = SinglyLinkedList()

        for i in range(len(sum_array)):    
            answer.add(ListNode(sum_array[i]))
        print([node.val for node in answer])

        return [node.val for node in answer]


        
     
       
        
     


        
        
        
        


# test code

# create 2 linked lists that represent numbers to be added
input1 = [2,4,3]
input2 = [5,6,4]



list1 = SinglyLinkedList()
list2 = SinglyLinkedList()




# create linked list 1

for i in range(len(input1)):    
    list1.add(ListNode(input1[i]))


# create linked list 2

for i in range(len(input2)):    
    list2.add(ListNode(input2[i]))


# show lists
# print([node.val for node in list1])
# print([node.val for node in list2])

# add addTwoNumbers
Solution().addTwoNumbers(list1,list2)

        

