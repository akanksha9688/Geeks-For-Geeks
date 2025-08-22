class Solution:
    def is_valid(self, arr, n, k, max_pages):
        students = 1
        current_sum = 0

        for pages in arr:
            if current_sum + pages > max_pages:
                students += 1
                current_sum = pages
                if students > k:  # More students needed than allowed
                    return False
            else:
                current_sum += pages
        return True

    def findPages(self, arr, k):
        n = len(arr)
        if k > n:  # Impossible if more students than books
            return -1

        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(arr, n, k, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
    
