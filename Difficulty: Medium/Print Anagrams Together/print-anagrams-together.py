#User function Template for python3
from collections import defaultdict


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        
        # Dictionary to hold sorted string as key and list of anagrams as values
        
        anagram_groups= defaultdict(list)
    
        # Group words by their sorted character strings
        for word in arr:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    
        # Collect groups in the order of their first appearance in the input
        result = list(anagram_groups.values())
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends