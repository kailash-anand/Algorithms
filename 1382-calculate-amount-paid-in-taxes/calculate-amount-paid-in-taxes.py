class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0.0
        prev = 0.0

        for bracket in brackets:
            upper = bracket[0]
            percent = bracket[1] / 100

            if income <= upper:
                tax += (income - prev) * percent
                break
            else:
                tax += (upper - prev) * percent
                prev = upper

        return tax