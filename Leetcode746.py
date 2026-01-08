class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = [-1] * len(cost)

        def optimal(i):
            if i >= len(cost):
                return 0

            if L[i] != -1:
                return L[i]

            alt1 = optimal(i+1) 
            alt2 = optimal(i+2)

            ret = cost[i] + min(alt1, alt2) 

            L[i] = ret

            return ret

        return min(optimal(0), optimal(1))

