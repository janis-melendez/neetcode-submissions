# Appoaches: 
#   A. Simulation - O(n^2) time, O(n) space <- optimal
#   B. Counting - O(n) time, O(1) space <- optimal
# Key Insights: 
#   1. Student ORDER does not matter - only counts of each preference (0 and 1)
#   2. End condition: top sandwich preference count == 0 -> everyone left is stuck
#   3. Invariant: sandwiches are consumed front-to-back, never skipped.
#      So walk sandwiches once, decremetn counts, stop at first exhausted type.

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 1. hash student preferences
        n = len(students)
        preferences = Counter(students)

        # 2. walk through sandwiches
        for sandwich in sandwiches:
            if preferences[sandwich] > 0:
                n -= 1
                preferences[sandwich] -= 1
            else:
                break
        
        # 3. return number of students left
        return n