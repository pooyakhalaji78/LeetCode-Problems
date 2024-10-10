# @title problem 2: Number to List
from typing import List
class Solution:
    def addTwoNumbers(self, l1: List[int], l2: List[int]) -> List[int]:
        final_l1 = 0
        final_l2 = 0
        i=0
        j=0
        z=1
        number_l10=[]
        for numbers_l1 in l1:
            number_l3= numbers_l1 * (10**i)
            final_l1 = number_l3 + final_l1
            i += 1
        print(f'number 1: {final_l1}')
        for numbers_l2 in l2:
            number_l4= numbers_l2 * (10**j)
            final_l2 = number_l4 + final_l2
            j += 1
        print(f'number 2: {final_l2}')

        final_number = final_l1 + final_l2
        print(f'final number: {final_number}')

        for z in range(len(str(final_number+1))):
        #while len(str(final_number))!=0:
          temp = final_number % 10
          final_number = int(final_number / 10)
          number_l10.append(temp)

        print(number_l10)




l1=[2,4,3]
l2=[5,6,4]
solution = Solution()
solution.addTwoNumbers(l1, l2)