class Solution {
  public:
    int majorityElement(vector<int>& arr) {
        // code here
        int ans = arr[0];
        int count = 1;

        for(int i=1; i<arr.size(); i++) {
            if(count == 0) ans = arr[i];
            if(ans == arr[i]) count++;
            else count--;
        }

        count = 0;
        for(int i=0; i<arr.size(); i++) {
            if(ans == arr[i]) count++;
        }

        if(count <= arr.size()/2) return -1;
        return ans;
    }
};
