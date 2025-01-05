#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        i, j = 0, n - 1
        count = 0
    
        # Step 2: Use two-pointer technique
        while i < j:
            if arr[i] + arr[j] < target:
                count += (j - i)  # Count all pairs from i to j
                i += 1
            else:
                j -= 1  # Decrease j to reduce the sum
        
        return count

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends