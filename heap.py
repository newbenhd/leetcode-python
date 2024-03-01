from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def formatList(self) -> List[int]:
        output = [self.val]
        if self.next:
            output.extend(self.next.formatList())
        return output

    def formatStr(self) -> str:
        return str(self.val) + (
            ("," + self.next.formatStr()) if self.next is not None else ""
        )


class Solution:
    def merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a and not b:
            return None
        if not a:
            return b
        if not b:
            return a
        head = ListNode(-1)
        tail = head
        while a and b:
            if a.val > b.val:
                tail.next = b
                b = b.next
                tail = tail.next
            else:
                tail.next = a
                a = a.next
                tail = tail.next
        if a:
            tail.next = a
        if b:
            tail.next = b
        return head.next

    def mergeInt(self, a: List[int], b: List[int]) -> List[int]:
        if not a and not b:
            return []
        if not a:
            return b
        if not b:
            return a
        if a[0] > b[0]:
            output = [b[0]]
            output.extend(self.mergeInt(a, b[1:]))
            return output
        else:
            output = [a[0]]
            output.extend(self.mergeInt(a[1:], b))
            return output

    def mergeSort(self, a: List[int]) -> List[int]:
        if len(a) == 0:
            return []
        if len(a) == 1:
            return a
        if len(a) == 2:
            return a if a[0] < a[1] else [a[1], a[0]]
        mid = len(a) // 2
        left = self.mergeSort(a[:mid])
        right = self.mergeSort(a[mid:])
        return self.mergeInt(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)
