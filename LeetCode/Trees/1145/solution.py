"""
Notes :
    1. Player1 picks a node.
    2. Player2 picks a node. He can chose from either left child, right child or parent (depending on which one has max nodes in their vicinity) of the node picked by player1. Assume he picks one. 
    3. Count number of nodes under player1 and player2. 
        a. If the number of nodes available for player2 > player1 => player2 wins. 
        b. Else                                                   => player1 wins.
    4. Equal case will never arise since there are an ODD number of nodes in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        x_node = self.findNode(x,root)
        l_count = self.countNodes(x_node.left)
        r_count = self.countNodes(x_node.right)
        p_count = n - (l_count + r_count + 1)
        
        return any([p_count>l_count+r_count, l_count>p_count+r_count, r_count>p_count+l_count])
    
    def findNode(self, int, root) :
        if root is None :
            return root 
        found = False
        
        if root.val == int:
            return root
        if root.left :
            found = self.findNode(int, root.left)
        if found :
            return found
        else :
            return self.findNode(int, root.right)
    
    def countNodes(self, root) :
        if root is None :
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)