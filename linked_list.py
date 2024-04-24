from typing import Optional, List


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
    def mergeKListsBinary(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        if N == 0:
            return None
        if N == 1:
            return lists[0]
        if N == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        left = self.mergeKListsBinary(lists[: N // 2])
        right = self.mergeKListsBinary(lists[N // 2 :])
        return self.mergeTwoLists(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, tail = None, None
        while lists:
            min_i = 0
            for i in range(1, len(lists)):
                if not lists[min_i]:
                    min_i = i
                elif lists[i] and lists[i].val < lists[min_i].val:
                    min_i = i
            if not lists[min_i]:
                # when every list is None
                break
            if not head or not tail:
                head = tail = lists[min_i]
                lists[min_i] = lists[min_i].next
            else:
                tail.next = lists[min_i]
                tail = tail.next
                lists[min_i] = lists[min_i].next
        return head

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
