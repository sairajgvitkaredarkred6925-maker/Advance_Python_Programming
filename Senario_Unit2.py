# 7. Longest Common Subsequence (LCS)
def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example usage
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of LCS:", lcs_length(s1, s2))

# 8. Longest Common Substring
def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0  # reset when characters don't match

    return max_len


# Example usage
s1 = "abcdxyz"
s2 = "xyzabcd"
print("Length of Longest Common Substring:", longest_common_substring(s1, s2))
