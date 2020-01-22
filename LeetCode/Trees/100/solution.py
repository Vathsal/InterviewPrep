"""
1. DATA STRUCTURES USED ?
    Stack
2. TYPE OF PROBLEM PATTERN ?
    DFS - Preorder
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S(worst)=O(N), S(best)= O(logN)
5. SOLUTION :
    DFS - Preorder traversal - Recursive
        1. Both trees are empty 
        2. One tree is empty 
        3. Both trees are non-empty 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#----------------------------------------------------------------------------------
# Q. Given 2 binary trees, write a function to check if they are the same or not.
#----------------------------------------------------------------------------------

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None :
            return True 
        
        if p is None or q is None :
            return False 
        
        areNodesSame = p.val == q.val
        areLeftSubTreesSame = self.isSameTree(p.left, q.left)
        areRightSubTreesSame = self.isSameTree(p.right, q.right)
        
        return areNodesSame and areLeftSubTreesSame and areRightSubTreesSame        