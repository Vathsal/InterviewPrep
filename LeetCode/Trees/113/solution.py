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
    NOTE : We cannot do reccursion with just the current function. 
           Hence we need to have a new function with additional parameters.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#---------------------------------------------------------------------------------
# Q. Given a binary tree and a sum, find all root-to-leaf paths where each path's 
#    sum equals the given sum.
#---------------------------------------------------------------------------------

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result_list = []
        self.pathSumHelper(root, [], result_list, sum)
        return result_list
      
    def pathSumHelper(self, root: TreeNode, sum: int, currentPath: List[int], allPaths: List[List[int]]) :
        if root is None :
            return allPaths 
        
        currentPath.append(root.val)            
        if root.left is None and root.right is None :
            if root.val == sum :
                allPaths.append(currentPath)
                return  
        self.pathSumHelper(root.left, sum-root.val, currentPath.copy(), allPaths)
        self.pathSumHelper(root.right, sum-root.val, currentPath.copy(), allPaths) 
        
