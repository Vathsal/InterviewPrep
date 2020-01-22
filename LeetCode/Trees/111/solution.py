"""
1. DATA STRUCTURES USED ?
    STACK
2. TYPE OF PROBLEM PATTERN ?
    DFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY : (RECURSIVE & ITERATIVE) 
    a. T=O(N)
a
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

#------------------------------------------------
# Q. Given a binary tree, find its minimum depth.
#------------------------------------------------

# ITERATIVE SOLUTION 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_depth = float('inf')
        
        if root is None:
            return 0
        
        temp_stack = [(root, 1)]
        while temp_stack:
            curr_node, curr_depth = temp_stack.pop()
            if curr_node:
                temp_stack.append((curr_node.left, curr_depth+1))
                temp_stack.append((curr_node.right, curr_depth+1))
                if curr_node.left is None and curr_node.right is None :
                    min_depth = min(min_depth, curr_depth)
                    
        return min_depth

# RECURSIVE SOLUTION 
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