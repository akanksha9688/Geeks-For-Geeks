class Solution:
    def subarrayXor(self, arr, k):
        # code here
        freq = {0: 1}  # To handle the case when prefixXOR == k
        prefixXOR = 0
        count = 0
        
        for num in arr:
            prefixXOR ^= num  # Calculate prefix XOR
            
            # Check if (prefixXOR ^ k) exists in freq
            targetXOR = prefixXOR ^ k
            count += freq.get(targetXOR, 0)
            
            # Update the frequency of the current prefixXOR
            freq[prefixXOR] = freq.get(prefixXOR, 0) + 1
        
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends