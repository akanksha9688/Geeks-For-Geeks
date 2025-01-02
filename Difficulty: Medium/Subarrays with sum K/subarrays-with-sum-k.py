#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        # Hash map to store the count of prefix sums
        prefix_count = {0: 1}  # Initialize with 0 to handle subarrays starting from index 0
        prefix_sum = 0
        count = 0
        
        for num in arr:
            # Update the prefix sum
            prefix_sum += num
            
            # Check if there exists a prefix_sum - k in the map
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            # Update the hash map with the current prefix sum
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends