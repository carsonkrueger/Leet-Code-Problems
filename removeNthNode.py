# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        first_head = head
        nthNodeBehind = head

        while (head):
            if i > n:
                nthNodeBehind = nthNodeBehind.next
            head = head.next
            i += 1
            
        if (nthNodeBehind.next):
            if (i == n):
                first_head = first_head.next
            nthNodeBehind.next = nthNodeBehind.next.next
            return first_head
        


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
    list = [1,2,3,4,5]
    head = nodes_from_list(list)
    node = sol.removeNthFromEnd(head, 2)
    print_listnode(node)

    list = [1]
    head = nodes_from_list(list)
    node = sol.removeNthFromEnd(head, 1)
    print_listnode(node)

    list = [1,2]
    head = nodes_from_list(list)
    node = sol.removeNthFromEnd(head, 2)
    print_listnode(node)