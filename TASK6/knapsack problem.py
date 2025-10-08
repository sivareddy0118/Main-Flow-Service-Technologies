# 0/1 Knapsack Problem using Dynamic Programming

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value in Knapsack =", dp[n][capacity])
