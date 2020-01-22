"""
1. DATA STRUCTURES USED ?
    NA
2. TYPE OF PROBLEM PATTERN ?
    Tree
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S=O(1)
5. SOLUTION :
    DFS - Preorder traversal - a. Recursive
                               b. Iterative
"""    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = 0 
        
        if root is None :
            return min_depth 
        
        min_depth = 1 
        left_tree_depth = self.minDepth(root.left)
        right_tree_depth = self.minDepth(root.right)
        
        if root.left is None :
            return min_depth + right_tree_depth
        elif root.right is None :
            return min_depth + left_tree_depth
        else :
            return min_depth + min(left_tree_depth, right_tree_depth)        