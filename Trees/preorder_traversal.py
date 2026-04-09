/*
Problem: prerder Traversal
Topic: Trees
Difficulty: Easy

Approach:
- Use recursion
- Traverse Root → Left → Right

Time Complexity: O(n)
Space Complexity: O(h)
*/

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pre(self,root,ans):
        
        if root==None:
            return
        
        # NLR
        
        ans.append(root.data)
        
        self.pre(root.left,ans)
        
        self.pre(root.right,ans)
        
        
    def preOrder(self, root):
    # code here
        ans=[]
        self.pre(root,ans)
        return ans
