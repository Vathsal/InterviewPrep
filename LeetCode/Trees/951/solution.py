"""
1. DATA STRUCTURES USED ?
    Stack
2. TYPE OF PROBLEM PATTERN ?
    DFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(min(N)1,N2))
    b. S=O(min(N)1,N2)
5. SOLUTION :
    DFS - Preorder traversal - Recursive
        1. Both trees are empty 
        2. One tree is empty 
        3. Both trees are non-empty 
            a. trees are same : left1 == left2 and right1 == right2
            b. trees are flipped : left1 == right2 and right1 == left2
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#-------------------------------------------------------------------------------------
# Q. Given 2 binary trees, determine whether the two binary trees are flip equivalent.
#    A binary tree X is flip equivalent to a binary tree Y if and only if we can make 
#    X equal to Y after some number of flip operations.
#-------------------------------------------------------------------------------------

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None :
            return True 
        
        if root1 is None or root2 is None :
            return False 
        
        if root1.val != root2.val :
            return False
        
        areLeftSubTreesSame = self.flipEquiv(root1.left, root2.left)
        areRightSubTreesSame = self.flipEquiv(root1.right, root2.right)
        areLeftAndRightFlipped = self.flipEquiv(root1.left, root2.right)
        areRightAndLeftFlipped = self.flipEquiv(root1.right, root2.left)
        
        return areLeftSubTreesSame and areRightSubTreesSame or areLeftAndRightFlipped and areRightAndLeftFlipped

