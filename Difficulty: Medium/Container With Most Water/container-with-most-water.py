
class Solution:
    def maxWater(self, arr):
        # code here
        # Initialize two pointers
        left, right = 0, len(arr) - 1
        max_area = 0
        
        # Traverse the array using two pointers
        while left < right:
            # Calculate the current area
            height = min(arr[left], arr[right])
            width = right - left
            current_area = height * width
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area



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