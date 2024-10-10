# @title problem 6: Length of Last Word
from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      list_words = []
      #using the .split function
      return len(s.split()[-1])

      ##my method
      # break_condition = 0
      # for i in range(len(s)-1,0,-1):
      #   if break_condition == 1:
      #     break
      #   if s[i]!=" ":
      #     j=i
      #     while s[j]!=" ":
      #       list_words.append(s[j])
      #       j-=1
      #       break_condition = 1
      # print(list_words)


#----------------------------------------------------
s = "   fly me   to   the moon  "
solution = Solution()
solution.lengthOfLastWord(s)