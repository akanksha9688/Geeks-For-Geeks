# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = 0
        max_len = 0
        sum_map = {}  # Dictionary to store the first occurrence of each prefix sum
    
        for i in range(len(arr)):
            prefix_sum += arr[i]
    
            # Check if current prefix sum equals k
            if prefix_sum == k:
                max_len = i + 1
    
            # Check if (prefix_sum - k) exists in the hash map
            if (prefix_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])
    
            # Store the prefix sum in the map if not already present
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
    
        return max_len
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends