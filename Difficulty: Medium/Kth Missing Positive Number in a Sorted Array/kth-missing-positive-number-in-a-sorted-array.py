#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
    
        # Binary search for the point where the missing count >= k
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            missing_count = arr[mid] - (mid + 1)
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # If left == 0, the kth missing is before the first element
        if left == 0:
            return k
        else:
            # Find kth missing using the last valid index (left - 1)
            missing_before = arr[left - 1] - (left)
            return arr[left - 1] + (k - missing_before)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends