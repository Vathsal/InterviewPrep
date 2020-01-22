"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root 
        
        temp_queue = [root]
        temp_queue.append(None)
        
        while temp_queue :
            curr_node = temp_queue.pop(0)
            if curr_node :
                curr_node.next = temp_queue[0]
                if curr_node.left:
                    temp_queue.append(curr_node.left)
                if curr_node.right:
                    temp_queue.append(curr_node.right)
            else :
                if len(temp_queue) > 0 :
                    temp_queue.append(None)
                    
        return root 