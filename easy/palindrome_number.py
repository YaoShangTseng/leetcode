class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    str_num = str(x)
    full_length = len(str_num)
    half_legnth = len(str_num) / 2
    if str_num[:(half_legnth)] == str_num[(full_length-half_legnth):][::-1]:
      return True
    else:
      return False
