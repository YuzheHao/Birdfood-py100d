# 100. Same Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # p and q are both None
        if not p and not q: # 这种直接用对None来操作的手法要记住
            return True
        
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        
        # both p and q are not None and equal
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

'''
使用递归的时候，函数的操作越精简越好
啥也不要管，直接扔给他做操作就好了
'''   