# Solve the rodcutting problem using dynamic programming.
# A bottom up solution:
def rod_cutting(prices, n):
    # Create a list to store the maximum revenue for each length
    max_revenue = [0] * (n + 1)

    # Build the max_revenue list in a bottom-up manner
    for length in range(1, n + 1): # length: length of the rod
        max_rev = float('-inf')
        for cut_length in range(1, length + 1):
            if cut_length <= len(prices):
                max_rev = max(max_rev, prices[cut_length - 1] + max_revenue[length - cut_length])
        max_revenue[length] = max_rev

    return max_revenue[n]

# Example usage:
if __name__ == "__main__":
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