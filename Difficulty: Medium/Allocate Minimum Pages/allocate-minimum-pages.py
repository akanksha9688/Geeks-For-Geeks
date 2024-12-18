class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n = len(arr)
        
        # If there are fewer books than students, return -1
        if k > n:
            return -1
        
        # Binary search boundaries
        start = max(arr)  # Minimum possible value of max pages
        end = sum(arr)    # Maximum possible value of max pages
        result = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if it's possible to allocate with mid as the maximum pages
            if self.is_possible(arr, n, k, mid):
                result = mid  # Store the valid allocation
                end = mid - 1  # Try to minimize the max pages further
            else:
                start = mid + 1  # Increase the allowed max pages
        
        return result

    # Helper function to check if a given allocation is possible
    def is_possible(self, arr, n, k, max_pages):
        students = 1
        current_sum = 0
        
        for pages in arr:
            # If a single book exceeds the allowed max_pages, allocation is impossible
            if pages > max_pages:
                return False
            
            # If adding this book exceeds the max_pages, allocate to the next student
            if current_sum + pages > max_pages:
                students += 1
                current_sum = pages
                
                # If more students are needed than available, return False
                if students > k:
                    return False
            else:
                current_sum += pages
        
        return True





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends