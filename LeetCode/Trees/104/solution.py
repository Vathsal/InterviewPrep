"""
1. DATA STRUCTURES USED ?
    STACK
2. TYPE OF PROBLEM PATTERN ?
    DFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY : (RECURSIVE & ITERATIVE) 
    a. T=O(N)
    b. S(worst)=O(N), S(best)= O(logN)
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
# Q. Given a binary tree, find its maximum depth.
#------------------------------------------------

# ITERATIVE SOLUTION 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0 
        
        if root is None :
            return max_depth 
        
        temp_stack = [(root, 1)]
        
        while temp_stack :
            curr_node, curr_depth = temp_stack.pop()
            if curr_node :
                temp_stack.append((curr_node.right, curr_depth+1))
                temp_stack.append((curr_node.left, curr_depth+1))
                max_depth = max(max_depth, curr_depth)
        
        return max_depth

# RECURSIVE SOLUTION 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0 
        
        if root is None :
            return max_depth 
        
        max_depth = 1 
        left_tree_depth = self.maxDepth(root.left)
        right_tree_depth = self.maxDepth(root.right)
        
        return max_depth + max(left_tree_depth, right_tree_depth)

# RECURSIVE SOLUTION - Optimized
class Solution:
    def maxDepth(self, root: TreeNode) -> int:  
        if root is None :
            return 0 

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
