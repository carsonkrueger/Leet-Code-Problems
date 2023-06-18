from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        first = True

        while dummy and dummy.next:
            temp = dummy.next.next
            temp2 = dummy.next
            dummy.next.next = dummy
            if (first):
                head = temp2
                first = False
            dummy.next = temp
            dummy = temp2

        return head
    
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

    list1 = [1,2,4,7]
    list1 = nodes_from_list(list1)
    node = sol.swapPairs(list1)
    print_listnode(node)

    list1 = [1]
    list1 = nodes_from_list(list1)
    node = sol.swapPairs(list1)
    print_listnode(node)

    list1 = []
    list1 = nodes_from_list(list1)
    node = sol.swapPairs(list1)
    print_listnode(node)