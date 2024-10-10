# @title problem 3: Palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0:
        return False
      else:
        i=0
        i_even=0
        i_odd=0
        list_version = []
        for i in range(len(str(x))):
          temp = x % 10
          x = int(x / 10)
          list_version.append(temp)
          i += 1
        print(f'list itself: {list_version}')
        print(f'length of list: {len(list_version)}')

        #for even values
        if len(str(x)) % 2 == 0:
          for i_even in range(len(list_version)/2):
            if list_version[i_even] != list_version[-(i_even+1)]:
              return False
          else:
            return True
            i_even += 1

        #for one length values
        if len(list_version) == 1:
            return True

        #for odd values
        if len(str(x)) % 2 != 0:
          print(int(len(list_version)/2))
          for i_odd in range(int(len(list_version)/2)):
            print(f'i_oddddd: {i_odd}')
            if list_version[i_odd] != list_version[-(i_odd+1)]:
              return False
          else:
            return True
            i_odd += 1

x=1000021
solution = Solution()
print(f'Is {x} a palindrome? {solution.isPalindrome(x)}')