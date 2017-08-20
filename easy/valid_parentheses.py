class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    arr = []
    for i in range(len(s)):
      if len(arr) == 0:
        arr.append(s[i])
        continue
      if s[i] == ')':
        if arr[-1] == '(':
          arr.pop()
        else:
          arr.append(s[i])
      elif s[i] == ']':
        if arr[-1] == '[':
          arr.pop()
        else:
          arr.append(s[i])
      elif s[i] == '}':
        if arr[-1] == '{':
          arr.pop()
        else:
          arr.append(s[i])
      else:
        arr.append(s[i])
    if len(arr) == 0:
      return True
    else:
      return False
