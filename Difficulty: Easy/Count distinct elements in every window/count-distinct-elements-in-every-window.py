
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        if n < k:
            return []  # If the array size is smaller than the window size, no windows exist.
    
        result = []  # To store the count of distinct elements in each window
        freq_map = {}  # Hash map to store the frequency of elements in the current window
    
        # Process the first window
        for i in range(k):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
        result.append(len(freq_map))
    
        # Slide the window
        for i in range(k, n):
            # Remove the element going out of the window
            element_out = arr[i - k]
            freq_map[element_out] -= 1
            if freq_map[element_out] == 0:
                del freq_map[element_out]
    
            # Add the new element coming into the window
            element_in = arr[i]
            freq_map[element_in] = freq_map.get(element_in, 0) + 1
    
            # Append the count of distinct elements in the current window
            result.append(len(freq_map))
    
        return result


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends