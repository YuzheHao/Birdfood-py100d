# 107. Binary Tree Level Order Traversal II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         def birth(root_list,box):
#             son = []
#             this_run = []
#             for root in root_list:
#                 small_box = []
#                 if not root: continue
                    
#                 if not root.left: 
#                     son.append(None)
#                 else:
#                     son.append(root.left)
#                     small_box.append(root.left.val)
#                 if not root.right:
#                     son.append(None)
#                 else:
#                     son.append(root.right)
#                     small_box.append(root.right.val)

#                 if len(small_box)!=0:
#                     this_run += small_box
#             if len(this_run)!= 0:
#                 box.append(this_run)
#             return son,box
        
#         if not root: return []
#         else:
#             son = [root]
#             box = [[root.val]]
#             while len(son)!=0:
#                 son,box = birth(son,box)
#             box.reverse()
#             return box


    # stack methods
    # 括号套括号的方式不可避免
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [root] # It captures the root node at the very beginning.
        levelOutput = [] # It captures the node values that are at the same level.
        output = [] # End result
        if root is None: # If the root is empty, return None.
            return (None)
        while stack:
            slen = len(stack)
            while slen > 0: # Keep traversing at the same level.
                temp = stack.pop(0)
                levelOutput.append(temp.val)
                if temp.left != None:
                    stack.append(temp.left)
                if temp.right != None:
                    stack.append(temp.right)
                slen -= 1
            output.append(levelOutput.copy())
            levelOutput.clear()
        return(output[::-1]) # Reverse the 2D list.
        