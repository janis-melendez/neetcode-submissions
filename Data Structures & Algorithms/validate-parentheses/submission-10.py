class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        close_to_open = { "}": "{", "]": "[",")": "(" }

        for char in s:
            if char in close_to_open:
                if open_stack and open_stack[-1] == close_to_open[char]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(char)
        
        return len(open_stack) == 0