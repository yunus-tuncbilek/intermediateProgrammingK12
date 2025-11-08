# This is my solution for Christina's code for Leetcode 42

from typing import List

def trap(height: List[int]) -> int:
    def water_in_between(height, i, j, water):
        # adds up the water between i and j
        # everything between i and j have height less than i or j
        num = min(height[i], height[j])
        for b in range(i + 1, j):
            water[b] = num - height[b]
        return water
        
    i = 0
    water = [0] * len(height)
    while i < len(height):
        num = height[i]
        if num > 0 and i < len(height) - 1:
            j = i + 1
            nextnum = height[j]
            while nextnum < num and j < len(height) - 1:
                j += 1
                nextnum = height[j]

            if nextnum >= num:
                water = water_in_between(height, i, j, water)

            if nextnum < num:
                # # SOLUTION 1: WORKS BUT GETS TLE
                # # couldn't find any number that is at least num, so
                # #   search for the highest number after num
                # j = i + 1
                # max_index = j

                # while j < len(height):
                #     if height[j] > height[max_index]:
                #         max_index = j
                #     j += 1
                
                # water = water_in_between(height, i, max_index, water)

                # i = max_index

                # SOlUTION 2: SUCCESSFUL

                return sum(water) + trap(list(reversed(height[i:])))
            else:
                i = j

        else:
            i += 1

    # print(water)

    return sum(water)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
assert trap(height) == 6

height = [4,2,0,3,2,5]
assert trap(height) == 9