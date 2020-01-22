"""
1. DATA STRUCTURES USED ?
    Stack
2. TYPE OF PROBLEM PATTERN ?
    DFS - postorder
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    a. T=O(N)
    b. S=O(H)
5. SOLUTION :
    1. Each node asks its l/r childern the question : what is the balance of coins you have/need.
       The balance of coins is calculated as : curr.val + left_balance + right_balance - 1
       If coins are moving out, we doa  +1. If coins are moving in, we do a -1
    2. During this process, we also update the total number of coins 
6. ANS:
    https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.result_moves = 0 
        def dfs(root) :
            if root is None :
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.result_moves += abs(left) + abs(right)
            return root.val + left + right - 1
       
        dfs(root)
        return self.result_moves