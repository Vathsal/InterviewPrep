"""
1. DATA STRUCTURES USED ?
    List 
2. TYPE OF PROBLEM PATTERN ?
    DFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S=O(N)
5. SOLUTION :
        a. Do Inorder traversal of each tree (Since we need the final result in ascending order, we should use INORDER traversal )
        b. Merge the 2 lists while sorting them
           3 conditions to merge :
                - both lists are of the same width 
                - first list is longer 
                - second list is longer 

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#----------------------------------------------------------------------------
# Q. Given two binary search trees, return a list containing all the integers 
#    from both trees sorted in ascending order.
#----------------------------------------------------------------------------

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        dfs_list1, dfs_list2 = [], []
        self.traversal(root1, dfs_list1)
        self.traversal(root2, dfs_list2)
        return self.mergeAndSortLists(dfs_list1, dfs_list2)
        
    def traversal(self, currNode, result_list):
        if currNode is None :
            return result_list 
        
        if currNode:
            self.traversal(currNode.left, result_list)
            result_list.append(currNode.val)
            self.traversal(currNode.right, result_list)
            
        return result_list 

    def mergeAndSortLists(self, dfs_list1, dfs_list2) :
        i, j = 0, 0
        result_list = []
        N1 = len(dfs_list1)
        N2 = len(dfs_list2)
         
        if N1 == 0 :
            return dfs_list2
        if N2 == 0 :
            return dfs_list1
        
        while len(result_list) <= (N1+N2) :
            if dfs_list1[i] <= dfs_list2[j]:
                result_list.append(dfs_list1[i])
                i += 1 
            else :
                result_list.append(dfs_list2[j])
                j += 1
            
            if i == N1 :
                result_list += dfs_list2[j:]
                break
            if j == N2 :
                result_list += dfs_list1[i:]
                break
                
        return result_list