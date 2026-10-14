class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for el in operations:
            if el == "+":
                # record the sum of the prev 2 values
                sum_val = record[-1] + record[-2]
                record.append(sum_val)
            elif el == "D":
                # record double the prev. score
                double_val = record[-1] * 2 
                record.append(double_val)
            elif el == "C":
                # remove previous score
                record.pop()
            else:
                # assume value is num
                # record int
                record.append(int(el))

        return sum(record)