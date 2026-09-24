def lcs(seq1, seq2):
    """
    Compute the Longest Common Subsequence (LCS) between two sequences.
    Uses Dynamic Programming for efficiency.
    Time Complexity: O(m * n), where m and n are lengths of seq1 and seq2.
    """

    m, n = len(seq1), len(seq2)
    # Create DP table initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_str.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_str))


# Example usage
if __name__ == "__main__":
    seq1 = "AGGTAB"
    seq2 = "GXTXAYB"
    result = lcs(seq1, seq2)
    print(f"LCS of '{seq1}' and '{seq2}' is: '{result}'")
