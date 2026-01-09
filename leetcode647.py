# Solve Leetcode 647: Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/

# A center expansion solution for counting palindromic substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Helper function to expand around center
        def expandAroundCenter(left: int, right: int) -> int:
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd length palindromes
            expandAroundCenter(i, i)
            # Even length palindromes
            expandAroundCenter(i, i + 1)

        return count

# A two-dimensional DP solution for the same problem
class DPSolution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # In the end, dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)] 
        count = 0

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if s[start] == s[end]:
                    if length <= 2 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        count += 1

        return count