class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # + - sum 2 previous values
        # D - double the prev value
        # C - remove previous score

        record = []

        for op in operations:
            if op == "+":
                two_sum = record[-1] + record[-2]
                record.append(two_sum)
            elif op == "D":
                double = record[-1] * 2
                record.append(double)
            elif op == "C":
                record.pop()
            else:
                num = int(op)
                record.append(num)
        
        return sum(record)