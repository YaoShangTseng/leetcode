class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
      return ''
    if len(strs) == 1:
      return strs[0]

    temp = list(strs[0])
    for str in strs:
      for i in range(len(temp)):
        if len(str) > i and str[i] == temp[i]:
          continue
        else:
          if i == 0:
            return ''
          else:
            temp = list(str[0:i])
            break
    return ''.join(temp)
