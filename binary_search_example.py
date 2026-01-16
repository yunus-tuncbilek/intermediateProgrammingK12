# Leetcode 278: First Bad Version
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n # establish the search boundaries

        while left < right: # continue until the boundaries converge
            guess = (left + right) // 2

            if isBadVersion(guess):
                right = guess # look for a bad version in the left half
            else:
                left = guess + 1 # look for a bad version in the right half

        return left # left is the first bad version. Note that left == right here