class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Track first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        # Find valid substrings starting at the first occurrence of each character
        for ch in first:
            i = first[ch]
            r = last[ch]
            valid = True

            j = i
            while j <= r:
                # If a character inside starts before i, i is not a valid start
                if first[s[j]] < i:
                    valid = False
                    break
                r = max(r, last[s[j]])
                j += 1

            if valid:
                valid_intervals.append((i, r))

        # Sort intervals by end index (Greedy choice)
        valid_intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for l, r in valid_intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans