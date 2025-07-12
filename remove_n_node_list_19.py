# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None
prev = None
for i in range(5):
    new_node = ListNode(i+1, None)
    # i+=1
    if head is None:
        head = new_node

    else:
        prev.next = new_node
    prev = new_node
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Step 1: Initialize a dummy node
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Step 2: Move the first pointer n + 1 steps ahead
    for _ in range(n + 1):
        first = first.next
        print(first.val)

    # Step 3: Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Step 4: Skip the target node
    second.next = second.next.next

    # Step 5: Return the new head
    return dummy.next


removeNthFromEnd(head, n = 2)

