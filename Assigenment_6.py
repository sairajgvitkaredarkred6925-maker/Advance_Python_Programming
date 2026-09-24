# 0/1 Knapsack Problem

# Top-Down (Recursive + Memoization)

def knapsack_top_down(weights, values, capacity):
    n = len(values)
    memo = {}

    def helper(i, w):
        if i == n or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]

        if weights[i] > w:
            result = helper(i + 1, w)
        else:
            # Option 1: Skip item
            skip = helper(i + 1, w)
            # Option 2: Take item
            take = values[i] + helper(i + 1, w - weights[i])
            result = max(skip, take)

        memo[(i, w)] = result
        return result

    return helper(0, capacity)



# Bottom-Up (Iterative DP)

def knapsack_bottom_up(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]



# Example Usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print("Top-Down Result:", knapsack_top_down(weights, values, capacity))
    print("Bottom-Up Result:", knapsack_bottom_up(weights, values, capacity))
