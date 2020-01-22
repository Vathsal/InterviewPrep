"""
1. DATA STRUCTURES USED ?
    STACK
2. TYPE OF PROBLEM PATTERN ?
    DFS 
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S=O(H)
5. SOLUTION :
        
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        N -= 1
        if N == 0 :
            return [TreeNode(0)]
        
        result_list = []
        for i in range(1, N, 2) :
            for left in self.allPossibleFBT(i) :
                for right in self.allPossibleFBT(N-i) :
                    root = TreeNode(0)
                    root.left = left
                    root.right = right 
                    result_list.append(root)
        
        return result_list  