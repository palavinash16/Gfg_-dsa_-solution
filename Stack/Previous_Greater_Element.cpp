// Problem: Previous Greater Element
// Platform: GeeksforGeeks
// Difficulty: Medium
// Approach: Monotonic Stack
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
  public:
    vector<int> preGreaterEle(vector<int>& arr) {
        int n = arr.size();
        vector<int> result;
        stack<int> st;   // stack to store elements
        
        for(int i = 0; i < n; i++) {
            
            // Remove all smaller or equal elements
            while(!st.empty() && st.top() <= arr[i]) {
                st.pop();
            }
            
            // If stack is empty → no greater element
            if(st.empty()) {
                result.push_back(-1);
            } else {
                result.push_back(st.top());
            }
            
            // Push current element
            st.push(arr[i]);
        }
        
        return result;
    }
};
