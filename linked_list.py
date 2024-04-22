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
