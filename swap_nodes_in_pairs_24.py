# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None
prev = None
for i in range(4):
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
print('\n')


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # Iterate through the list while there are at least two nodes to swap
    while current.next and current.next.next:
        # Identify the nodes to swap
        first = current.next
        second = current.next.next

        # Swap the nodes
        # First's next should point to what Second was pointing to
        first.next = second.next
        # Second's next should point to First
        second.next = first
        # Current's next should now point to Second
        current.next = second

        # Move 'current' two nodes forward in the list
        current = first

    return dummy.next



head = swapPairs(head)
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print('\n')


