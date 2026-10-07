from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            # If valid strings at the current level are found, don't generate deeper states
            if found:
                continue

            # Generate all possible states by removing one parenthesis at a time
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result