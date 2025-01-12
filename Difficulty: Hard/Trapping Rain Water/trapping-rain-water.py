
class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        if n < 3:
            return 0  # Cannot trap water with less than 3 blocks
    
        # Step 1: Compute left_max array
        left_max = [0] * n
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
    
        # Step 2: Compute right_max array
        right_max = [0] * n
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
    
        # Step 3: Calculate total water trapped
        total_water = 0
        for i in range(n):
            total_water += max(0, min(left_max[i], right_max[i]) - arr[i])
    
        return total_water



#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends