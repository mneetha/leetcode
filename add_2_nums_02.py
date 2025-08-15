# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None
# prev = None
# for i, in range(4):
#     new_node = ListNode(i+1, None)
#     # i+=1
#     if head is None:
#         head = new_node
#
#     else:
#         prev.next = new_node
#     prev = new_node
#

def convert_num_rev_linked_list(num):
    num_node_head = None
    str_num_rept = str(num)
    for i in range(len(str_num_rept)):
        a_node = ListNode(int(str_num_rept[i]))
        if num_node_head is None:
            num_node_head = a_node
        else:
            a_node.next = num_node_head
            num_node_head = a_node

    curr = num_node_head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print('\n')

    return num_node_head

# num_1 = convert_num_rev_linked_list(342)
# num_2 = convert_num_rev_linked_list(465)
num_1 = convert_num_rev_linked_list(0)
num_2 = convert_num_rev_linked_list(0)
# num_1 = convert_num_rev_linked_list(9999999)
# num_2 = convert_num_rev_linked_list(9999)




def addTwoNumbers(l1, l2):

    cur_dummy1 = ListNode(0)
    cur_dummy1.next = l1
    cur_dummy2 = ListNode(0)
    cur_dummy2.next = l2
    ans_head = None
    cur_dummy = None

    carry_over = 0
    while cur_dummy1.next is not None and cur_dummy2.next is not None:
        print(f'num1: {cur_dummy1.next.val}')
        print(f'num2: {cur_dummy2.next.val}')

        answ_int = cur_dummy1.next.val + cur_dummy2.next.val +carry_over
        # reset the carry over
        if answ_int - 10 >= 0:
            #set carry_over
                carry_over = 1
                answ_int = answ_int-10
        else:
            carry_over = 0

        ans_node = ListNode(answ_int)
        if ans_head is None:
            ans_head = ans_node
        else:
            ans_node.next = ans_head
            ans_head = ans_node

        # check if either of the list is finished.
        cur_dummy1 = cur_dummy1.next
        cur_dummy2 = cur_dummy2.next
    if cur_dummy1.next is None:
        cur_dummy = cur_dummy2
    elif cur_dummy2.next is None:
        cur_dummy = cur_dummy1
    if cur_dummy is not None:
        #loop through cur_dummy
        while cur_dummy.next is not None:
            # add any carry over to cur number and
            answ_int = cur_dummy.next.val + carry_over
            # reset the carry over
            if answ_int - 10 >= 0:
                # set carry_over
                carry_over = 1
                answ_int = answ_int - 10
            else:
                carry_over = 0
            # create new node
            ans_node = ListNode(answ_int)
            ans_node.next = ans_head
            ans_head = ans_node
            cur_dummy = cur_dummy.next
    if carry_over ==1:
        ans_node = ListNode(carry_over)
        ans_node.next = ans_head
        ans_head = ans_node
    return ans_head

head = addTwoNumbers(num_1, num_2)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print('\n')


