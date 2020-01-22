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

#--------------------------------------------------------------------------------------------------
# Q. Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#--------------------------------------------------------------------------------------------------

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None :
            return True 
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, leftNode: TreeNode, rightNode: TreeNode) :
        if leftNode is None and rightNode is None :
            return True 
        
        if leftNode is None or rightNode is None :
            return False 
        
        areNodesSame = leftNode.val == rightNode.val 
        areleftSubTreesSame = self.isSymmetricHelper(leftNode.left, rightNode.right)
        areRightSubTreesSame = self.isSymmetricHelper(leftNode.right, rightNode.left)
        
        return areNodesSame and areleftSubTreesSame and areRightSubTreesSame

