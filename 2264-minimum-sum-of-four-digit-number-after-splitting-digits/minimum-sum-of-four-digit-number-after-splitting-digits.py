class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = list()

        for x in range(len(str(num))):
            num_list.append(str(num)[x])

        num_list.sort()

        num1 = int(num_list[0])*10 + int(num_list[3])
        num2 = int(num_list[1])*10 + int(num_list[2])

        return num1 + num2
        
        

        


