from typing import Optional


class ListNodeWithEqual:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListNodeWithEqual):
            return NotImplemented
        node = self
        while node and other:
            if node.val != other.val:
                return False
            node = node.next
            other = other.next
        return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoListsRecursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head, tail = None, None
        while list1 and list2:
            if list1.val > list2.val:
                if not tail:
                    tail = list2
                    head = list2
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next
            else:
                if not tail:
                    tail = list1
                    head = list1
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return head

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        turtle, rabbit = head, head.next
        while rabbit and turtle:
            if rabbit == turtle:
                return True
            if rabbit.next:
                rabbit = rabbit.next.next
            else:
                return False
            turtle = turtle.next
        return False

    def reverseList(
        self, head: Optional[ListNodeWithEqual]
    ) -> Optional[ListNodeWithEqual]:
        tail = None
        node = head
        while node:
            next = node.next
            node.next = tail
            tail = node
            node = next
        return tail
