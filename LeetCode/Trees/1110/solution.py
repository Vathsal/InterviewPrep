"""
1. DATA STRUCTURES USED ?
    Set()
2. TYPE OF PROBLEM PATTERN ?
    DFS - postorder
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S=O(N)
5. SOLUTION :
    - Use DFS to traverse the tree bottom up. 
      The recursive function removeNode is called on each node to decide if we need to keep the node or remove it. 
        a. If the node is present in the to_delete_set(), then the node is deleted and None is returned 
        b. If the node is not present in the to_delete_set(), then the node is return
6. VIDEO SOLUTION :
    https://www.youtube.com/watch?v=aaSFzFfOQ0o
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result_list = []
        to_delete_set = set(to_delete)
        
        self.removeNodes(root, to_delete_set, result_list)
        if root.val not in to_delete_set:
            result_list.append(root)
            
        return result_list 
    
    def removeNodes(self, currNode, to_delete_set, result_list) :
        if currNode is None :
            return currNode 
        
        currNode.left = self.removeNodes(currNode.left, to_delete_set, result_list)
        currNode.right = self.removeNodes(currNode.right, to_delete_set, result_list)
        
        if currNode.val in to_delete_set :
            if currNode.left :
                result_list.append(currNode.left)
            if currNode.right :
                result_list.append(currNode.right)
            return None #remove node
    
        return currNode #keep node
        