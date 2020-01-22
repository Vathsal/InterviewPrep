"""
1. DATA STRUCTURES USED ?
    Stack
2. TYPE OF PROBLEM PATTERN ?
    DFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S(worst)=O(N), S(best)= O(logN)
5. SOLUTION :
    DFS - Preorder traversal - a. Recursive
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#---------------------------------------------------------------------------------
# Q. Given a binary tree and a sum, determine if the tree has a root-to-leaf 
#    path where the path sum equals the given sum.
#---------------------------------------------------------------------------------

# RECURSIVE SOLUTION 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None :
            return False 

        left_path_sum = self.hasPathSum(root.left, sum-root.val)
        right_path_sum = self.hasPathSum(root.right, sum-root.val)
        if root.left is None and root.right is None :
            if root.val == sum :
                return True 
            else :
                return False 
        
        return left_path_sum or right_path_sum

# ITERATIVE SOLUTION 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None :
            return False 

        temp_stack = [(root, sum)]
        while temp_stack :
            curr_node, curr_sum = temp_stack.pop()
            if curr_node :
                temp_stack.append((curr_node.left, curr_sum-curr_node.val))
                temp_stack.append((curr_node.right, curr_sum-curr_node.val))
                if curr_node.left is None and curr_node.right is None :
                    if curr_node.val == curr_sum :
                        return True 

        return False 
