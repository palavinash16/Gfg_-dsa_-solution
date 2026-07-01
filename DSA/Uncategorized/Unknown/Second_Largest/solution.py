class Solution:
def getSecondLargest(self, arr):
# code here
arrays=list(set(arr))
if len(arrays)<2:
return -1
arrays.sort(reverse=True)
return arrays[1]
