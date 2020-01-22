"""
1. DATA STRUCTURES USED ?
    Queue
2. TYPE OF PROBLEM PATTERN ?
    BFS
3. EDGE CASES / BASE CASE ?
    NA
4. COMPLEXITY :
    #1
    a. T=O(N)
    b. S=O(N)
    #2
    a. T=O(N)
    b. S=O(1)
5. SOLUTION #1:
    - REMEMBER : You need to return the node, not the list
                 Do BFS --> Iterative --> Queue 
    1. Append the root and then None to the queue
    2.  a. If the curr_node is None => you have reached the end of the queue, hence append another None to the list. 
        b. If the curr_node is not None => point the next pointer to the top of queue. Insert left and right nodes into the queue. 
        
   SOLUTION #2:
        1. Assign previous and current nodes. previous will be the leftmost node in that level. current will start from previous and move to the end
        2. Make the connection as necessary 
       
"""    

# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

#---------------------------------------------------------------------------------------------
# Q. Given a PERFECT BINARY TREE, populate each next pointer to point to its next right node. 
#    If there is no next right node, the next pointer should be set to NULL.
#    Perfect binary tree => all leaves are on the same level, and every parent has 2 children. 
#---------------------------------------------------------------------------------------------

# ITERATIVE SOLUTION 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None :
            return root 
        
        prev = root
        curr = None 
        while prev.left :
            curr = prev
            while curr :
                curr.left.next = curr.right 
                if curr.next :
                    curr.right.next = curr.next.left 
                curr = curr.next 
            prev = prev.left
  
        return root   


# RECURSIVE SOLUTION 
   def connect(self, root: 'Node') -> 'Node':
        if root is None :
            return root 
        
        temp_queue = [(root)]
        temp_queue.append(None)

        while temp_queue :
            curr_node = temp_queue.pop(0)
            if curr_node :
                curr_node.next = temp_queue[0] 
                if curr_node.left :
                    temp_queue.append(curr_node.left)
                if curr_node.right :
                    temp_queue.append(curr_node.right)
            else :
                if len(temp_queue) > 0 :
                    temp_queue.append(None)
  
        return root     