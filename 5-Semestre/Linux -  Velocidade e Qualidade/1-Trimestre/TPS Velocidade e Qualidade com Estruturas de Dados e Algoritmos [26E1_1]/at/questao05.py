import random
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def build_bst_random(n=20):
    vals = random.sample(range(1000), n)
    root = None
    for v in vals:
        if root is None:
            root = TreeNode(v)
            continue
        node = root
        while True:
            if v < node.val:
                if node.left is None:
                    node.left = TreeNode(v)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(v)
                    break
                node = node.right
    return root

def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

def depth_first_stack(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

print("QUESTAO 5: ")
tree = build_bst_random(20)
print("Nivel:", level_order(tree))
print("Profundidade:", depth_first_stack(tree))