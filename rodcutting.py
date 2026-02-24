# Solve the rodcutting problem using dynamic programming.
# A bottom up solution:
def rod_cutting(prices, n):
    # Create a list to store the maximum revenue for each length
    #### This is the DP array ####
    max_revenue = [0] * (n + 1)

    # Build the max_revenue list in a bottom-up manner
    # Time complexity: O(L^2) where L is the length of the longest rod
    for length in range(1, n + 1): # length: length of the rod
        max_rev = float('-inf')
        for cut_length in range(1, length + 1):
            if cut_length <= len(prices):
                # The revenue from cutting the rod into a piece of length cut_length (which costs prices[cut_length - 1])
                #   and the remaining piece of length (length - cut_length)
                max_rev = max(max_rev, prices[cut_length - 1] + max_revenue[length - cut_length])
        max_revenue[length] = max_rev

    return max_revenue[n]

# Example usage:
if __name__ == "__main__":
    # prices[i] is the price of a rod of length i+1
    # For example, rod of length 1 costs 1, length 2 costs 5, etc.
    prices = [1, 5, 8, 9, 10, 17, 17, 20] 
    n = 8
    print(f"Maximum revenue for rod of length {n}: {rod_cutting(prices, n)}")

# A top down solution:
def rod_cutting_top_down(prices, n):
    memo = {}

    def helper(length):
        if length == 0:
            return 0
        if length in memo:
            return memo[length]

        max_rev = float('-inf')
        for cut_length in range(1, length + 1):
            if cut_length <= len(prices):
                max_rev = max(max_rev, prices[cut_length - 1] + helper(length - cut_length))
        memo[length] = max_rev
        return max_rev

    return helper(n)