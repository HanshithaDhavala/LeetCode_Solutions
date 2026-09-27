class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until we find the matching '('
                rev = []
                while stack and stack[-1] != '(':
                    rev.append(stack.pop())
                # Remove the '(' from stack
                stack.pop()
                # Push back the reversed characters
                stack.extend(rev)
            else:
                stack.append(char)
                
        return "".join(stack)