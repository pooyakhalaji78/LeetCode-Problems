# @title problem 4: Longest Common Prefix
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if len(strs) == 0:
        return ""
      letter=0
      word=1
      output = ""
      temp=""
      condition = 0
      for letter in range(len(strs[0])):



        for word in range(len(strs)):


          if letter > len(strs[word])-1:
            condition = 1
            temp = ""
          elif (strs[0][letter] != strs[word][letter]):
            temp = ""
            condition = 1
          else:
            temp = strs[0][letter]

        if condition ==1:
          break


        output = output + temp


      return output

strs = ["aaa","aa","aaa"]
solution = Solution()
solution.longestCommonPrefix(strs)
