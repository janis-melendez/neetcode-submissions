def is_matching_bracket(open_char: str, end_char: str) -> bool:
    match open_char:
        case "{":
            return end_char == "}"
        case "(":
            return end_char == ")"
        case "[":
            return end_char == "]"
        case _:
            return False 

class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        is_valid = True
        
        for char in s:
            # if open bracket, push into stack
            if char == "{" or char == "[" or char == "(":
                open_stack.append(char) 
            # if back bracket, pop off the stack and compare. Return false if invalid
            elif char == "}" or char == "]" or char == ")":
                open_char = open_stack.pop() if len(open_stack) > 0 else -1
                end_char = char
                if is_matching_bracket(open_char, end_char) == False:
                    return False
            
        return len(open_stack) == 0