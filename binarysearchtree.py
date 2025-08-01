#Binary Trees
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

    def __str__(self):
        return str(self.val)

#        1
#     2    3
#   4  5  10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right =E
C.left = F
print(A)

#recursive pre order traversal DFS Time= O(n), space= O(n)
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# pre_order(A)

#recursive in order traversal DFS T=O(n), S=O(n)
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

# in_order(A)

#iterative Pre order Traversal DFS T=O(n), S=O(n)
def pre_order_iterative(node):
    stk = [node]
    while stk:
        node = stk.pop()
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
        print(node)
# pre_order_iterative(A)

#check if value exists DFS T=O(n), S=O(n)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)

print(search(A, 11))

# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# in_order(A2)

# time O(logn), space=O(logn)
def search_bst(node, target):
    if not node:
        return False

    if node.val ==target:
        return True

    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)

print(search_bst(A2, -1))

