class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungry_students = len(students)
        preferences = Counter(students)

        for sandwich in sandwiches:
            if preferences[sandwich] > 0:
                hungry_students -= 1
                preferences[sandwich] -= 1
            else:
                break
        
        return hungry_students
