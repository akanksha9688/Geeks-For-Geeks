class Solution:
    def maxLen(self, arr):
        # code here
        # Replace 0 with -1
        arr = [-1 if x == 0 else 1 for x in arr]
        
        prefix_sum = 0
        max_length = 0
        prefix_map = {0: -1}  # Initialize with 0 at index -1 to handle edge cases
    
        for i, num in enumerate(arr):
            prefix_sum += num
            
            # Check if prefix_sum has been seen before
            if prefix_sum in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
    
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends