# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)  # Calculate the total sum of the array
        left_sum = 0  # Initialize left sum to 0
        
        for i, value in enumerate(arr):
            # Calculate right sum by excluding the current element
            total_sum -= value
            
            # Check if left sum is equal to right sum
            if left_sum == total_sum:
                return i  # Return the current index as equilibrium point
            
            # Update left sum by adding the current element
            left_sum += value
        
        # If no equilibrium index is found
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends