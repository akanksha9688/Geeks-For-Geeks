class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        # Determine the dimensions of the matrix
        n = len(mat)          # Number of rows
        m = len(mat[0])       # Number of columns
    

        result = []
        top, bottom, left, right = 0, n - 1, 0, m - 1
    
        while top <= bottom and left <= right:
            # Traverse from left to right on the top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
    
            # Traverse from top to bottom on the rightmost column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
    
            # Traverse from right to left on the bottom row (if not already traversed)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
    
            # Traverse from bottom to top on the leftmost column (if not already traversed)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
    
        return result


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends