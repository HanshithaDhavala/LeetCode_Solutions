class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            # Check for a palindrome of length k or k + 1 starting at or after index i
            # (Any longer palindrome contains a smaller palindrome of length k or k + 1)
            found = False

            for j in range(i, n):
                # Check for length k palindrome ending at j
                if j - k + 1 >= i:
                    sub = s[j - k + 1 : j + 1]
                    if sub == sub[::-1]:
                        ans += 1
                        i = j + 1  # Move past this palindrome greedily
                        found = True
                        break

                # Check for length k + 1 palindrome ending at j
                if j - k >= i:
                    sub = s[j - k : j + 1]
                    if sub == sub[::-1]:
                        ans += 1
                        i = j + 1  # Move past this palindrome greedily
                        found = True
                        break

            if not found:
                break

        return ans