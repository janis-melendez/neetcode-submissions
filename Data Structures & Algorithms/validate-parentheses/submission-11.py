close_to_open = {
    "}": "{",
    ")": "(",
    "]": "["
}

class Solution:
    def isValid(self, s: str) -> bool:
        open_pairs = []

        for char in s:
            if char in close_to_open:
                if open_pairs and open_pairs[-1] == close_to_open[char]:
                    open_pairs.pop()
                else:
                    return False
            else:
                open_pairs.append(char)

        return len(open_pairs) == 0