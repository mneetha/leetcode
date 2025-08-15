# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None
for i in range(5):
    new_node = ListNode(i+1, None)
    # i+=1
    if head is None:
        head = new_node

    else:
        prev.next = new_node
    prev = new_node


def reverseKGroup(head, k):

    prev = None
    curr = head
    node_cnt = 0

    while curr!= None and k:
        node_cnt+=1
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


head = reverseKGroup(head, 4)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print('\n')


