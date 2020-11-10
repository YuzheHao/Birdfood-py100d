# 101. Symmetric Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:       
#         def box_check(box):
#             while len(box)!=0:
#                 if box[0] != box[-1]:
#                     return False
#                 else:
#                     box.pop(0)
#                     box.pop(-1)
#             return True
    
#         def birth_check(nodelist):
#             check_box = []
#             node_box = []
#             for parents in nodelist:
#                 if not parents: 
#                     return
#                 else:                    
#                     if not parents.left: 
#                         check_box.append('X')
#                     else: 
#                         check_box.append(parents.left.val)
#                         node_box.append(parents.left)
#                     if not parents.right: 
#                         check_box.append('X')
#                     else: 
#                         check_box.append(parents.right.val)
#                         node_box.append(parents.right)
#             return node_box, check_box
#         if not root:
#             return True
#         son = [root]
#         flag = True
#         while len(son) != 0:
#             son,check_box = birth_check(son)
#             if not box_check(check_box):
#                 return False
#         return True
        
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val) and isMirror(t1.right,t2.left) and isMirror(t1.left,t2.right)
        return isMirror(root,root)
            
                    
                    
                
                
                
            