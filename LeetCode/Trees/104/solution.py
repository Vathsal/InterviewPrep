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
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0 
        
        if root is None :
            return max_depth 
        
        # ITERATIVE SOLUTION 
        # max_depth = 1 
        # left_tree_depth = self.maxDepth(root.left)
        # right_tree_depth = self.maxDepth(root.right)
        #
        # return max_depth + max(left_tree_depth, right_tree_depth)
        
        # RECURSIVE SOLUTION 
        temp_stack = [(root, 1)]
        
        while temp_stack :
            curr_node, curr_depth = temp_stack.pop()
            if curr_node :
                temp_stack.append((curr_node.right, curr_depth+1))
                temp_stack.append((curr_node.left, curr_depth+1))
                max_depth = max(max_depth, curr_depth)
        
        return max_depth