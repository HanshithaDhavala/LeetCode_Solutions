class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res, cur = set(), [{""}]
        
        for i, c in enumerate(expression):
            if c.isalpha():
                # Concatenate current letter to all strings in the current set
                cur[-1] = {s + c for s in cur[-1]}
            elif c == '{':
                # Save current context and push onto stack
                stack.append((res, cur))
                res, cur = set(), [{""}]
            elif c == '}':
                # Evaluate the inside of the braces
                sub_res = res | cur[-1]
                res, cur = stack.pop()
                # Concatenate the evaluated set with the previous block
                cur[-1] = {a + b for a in cur[-1] for b in sub_res}
            elif c == ',':
                # Take union of current concatenated block into res
                res |= cur[-1]
                cur[-1] = {""}
        
        # Combine remaining sets and return sorted list
        final_set = res | cur[-1]
        return sorted(list(final_set))