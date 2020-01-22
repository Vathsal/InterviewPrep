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

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#---------------------------------------------------------------------------------
# Q. Given a binary tree and a sum, find the number of paths that sum to a given value.
#    The path does not need to start or end at the root or a leaf, but it must go downwards 
#    (traveling only from parent nodes to child nodes).
#---------------------------------------------------------------------------------

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.pathSumHelper(root, sum, [])
    
    def pathSumHelper(self, root:TreeNode, sum:int, currentPath:List[int]) -> int:
        path_count = 0 
        path_sum = 0
        
        if root is None :
            return path_count
        
        currentPath.append(root.val)
        for i in range(len(currentPath)-1, -1, -1):
            path_sum += currentPath[i]
            if path_sum == sum :
                path_count += 1            
        path_count += self.pathSumHelper(root.left, sum, currentPath)
        path_count += self.pathSumHelper(root.right, sum, currentPath)
        del currentPath[-1]
        
        return path_count

        