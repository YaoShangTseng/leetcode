class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    x_to_string = str(x)
    if x_to_string[0] == '-':
      answer = int(x_to_string[0] + x_to_string[1:][::-1])
    else:
      answer = int(x_to_string[0:][::-1])

    if ( answer > 2 ** 31 - 1) or ( answer < -1 * 2 ** 31 ):
      return 0
    else:
      return answer
