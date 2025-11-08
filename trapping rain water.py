# NOT WORKING:
#   It is not working when the highest element (called H) of the list height is
#   followed by an element that is not highest among
#   all elements to the right of H.

class Solution:
    def trap2(self, height: List[int]) -> int:
        i = 0
        water = 0
        while i < len(height):
            num = height[i]
            if num > 0 and i < len(height) - 1:
                j = i + 1
                nextnum = height[j]
                while nextnum < num and j < len(height) - 1:
                    j += 1
                    nextnum = height[j]

                if nextnum >= num:
                    for b in range(i + 1, j):
                        water += num - height[b]

                if nextnum < num:
                    i += 1
                else:
                    i = j

            else:
                i += 1

        return water

    def trap(self, height: List[int]) -> int:
        x = self.trap2(height)
        height.reverse()
        y = self.trap2(height)
        return max(x,y)