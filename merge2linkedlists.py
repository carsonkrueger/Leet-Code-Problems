# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3: Optional[ListNode] = ListNode(None)
        head = list3

        while (list1 and list2):
            if (list1.val <= list2.val):
                list3.next = list1
                list1 = list1.next
            elif (list2.val < list1.val):
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if (list1):
            list3.next = list1
        elif (list2):
            list3.next = list2

        return head.next

def nodes_from_list(list):
    cur_node = None

    for num in reversed(list):
        if (cur_node is None):
            cur_node = ListNode(num)
        else:
            next_node = ListNode(num)
            next_node.next = cur_node
            cur_node = next_node

    return cur_node

def print_listnode(node: ListNode):
    print("[", end="")
    while (node):
        print(node.val, end="")
        if (node.next):
            print(",",end="")
        node = node.next
    print("]",)

if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    list1 = nodes_from_list(list1)
    list2 = nodes_from_list(list2)
    node = sol.mergeTwoLists(list1, list2)
    print_listnode(node)

    list1 = []
    list2 = []
    list1 = nodes_from_list(list1)
    list2 = nodes_from_list(list2)
    node = sol.mergeTwoLists(list1, list2)
    print_listnode(node)

    list1 = []
    list2 = [0]
    list1 = nodes_from_list(list1)
    list2 = nodes_from_list(list2)
    node = sol.mergeTwoLists(list1, list2)
    print_listnode(node)