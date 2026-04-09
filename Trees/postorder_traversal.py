/*
Problem: post Traversal
Topic: Trees
Difficulty: Easy

Approach:
- Use recursion
- Traverse Left → Right → Node

Time Complexity: O(n)
Space Complexity: O(h)
*/

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def post(self,root,ans):
        
        if(root==None):
            return
        
        # L R N
        self.post(root.left,ans)
        self.post(root.right,ans)
        ans.append(root.data)
        
    def postOrder(self, root):
        # code here
        ans=[]
        self.post(root,ans)
        return ans
        
