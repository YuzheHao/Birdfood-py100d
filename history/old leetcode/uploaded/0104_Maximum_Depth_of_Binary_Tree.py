
# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     def walk(root,box,depth):
    #         if not root: 
    #             return box
    #         box.append(depth)
    #         depth += 1
    #         box = walk(root.left,box,depth)
    #         box = walk(root.right,box,depth)
    #         return box
    #     box =[]
    #     depth = 1
    #     walks = walk(root,box,1)
    #     if len(walks)==0: return 0
    #     else: return max(walks)
        
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0;
        if not root.left and not root.right: return 1
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth
            