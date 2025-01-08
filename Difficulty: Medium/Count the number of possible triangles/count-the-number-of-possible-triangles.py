#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
         # Sort the array
        arr.sort()
        n = len(arr)
        count = 0
    
        # Fix the largest side as arr[k]
        for k in range(2, n):
            i, j = 0, k - 1  # Two pointers
            while i < j:
                # Check the triangle condition
                if arr[i] + arr[j] > arr[k]:
                    # All pairs (i, i+1, ..., j-1, j) form valid triangles
                    count += (j - i)
                    j -= 1  # Decrease j to check other combinations
                else:
                    i += 1  # Increase i to try a larger sum
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends