# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        concatVal1 = concatVal2 = ""

        while(l1):
            concatVal1 = str(l1.val) + concatVal1
            l1 = l1.next

        while(l2):
            concatVal2 = str(l2.val) + concatVal2
            l2 = l2.next
            
        if not concatVal1:
            concatVal1 = "0"    

        if not concatVal2:
            concatVal2 = "0"

        sum = int(concatVal1) + int(concatVal2)
        initial = cur = ListNode()

        for i in reversed(str(sum)):
            cur.next = ListNode(int(i))
            cur = cur.next

        # print(initial.next)
        return(initial.next)