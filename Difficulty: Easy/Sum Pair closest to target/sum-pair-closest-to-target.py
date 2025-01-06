#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        # Edge case: If the array has fewer than 2 elements, return an empty array
        if len(arr) < 2:
            return []
    
        # Sort the array
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_pair = []
        closest_diff = float('inf')  # To track the smallest difference
        max_abs_diff = float('-inf')  # To track the maximum absolute difference
    
        while left < right:
            # Calculate the current sum
            current_sum = arr[left] + arr[right]
            current_diff = abs(target - current_sum)
    
            # Check if this pair is closer to the target
            if current_diff < closest_diff or (current_diff == closest_diff and abs(arr[right] - arr[left]) > max_abs_diff):
                closest_diff = current_diff
                max_abs_diff = abs(arr[right] - arr[left])
                closest_pair = [arr[left], arr[right]]
    
            # Adjust the pointers based on the sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If we find a perfect match, return the pair immediately
                return [arr[left], arr[right]]
    
        return closest_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends