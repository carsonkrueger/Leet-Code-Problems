from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        final = dummy = ListNode(0)
        tailsReached = 0
        listLen = len(lists)

        while (tailsReached < listLen):
            for i in range(listLen):
                minVal = 0

                if (lists[i].val == None):
                    tailsReached += 1
                    continue

                if (i == 0):
                    minVal = lists[i].val
                elif (lists[i].val < minVal):
                    minVal = lists[i].val

        
            