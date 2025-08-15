from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        s, f = head, head
        while f and f.next != None:
            print(s.val)
            print(f.val)
            s = s.next
            f = f.next.next
            if s == f:
                print(s.val)
                print(f.val)
                break

        if not f or not f.next:
            return None

        s = head
        while s != f:
            s = s.next
            f = f.next
            print(s.val)
            print(f.val)

        return s