class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    roman_hash = {}
    roman_hash["I"] = 1
    roman_hash["V"] = 5
    roman_hash["X"] = 10
    roman_hash["L"] = 50
    roman_hash["C"] = 100
    roman_hash["D"] = 500
    roman_hash["M"] = 1000
    sum = 0
    prev_char = ""
    for c in s[::-1]:
      if prev_char == "":
        prev_char = c
        sum += roman_hash.get(c)
        continue
      if roman_hash.get(c) >= roman_hash.get(prev_char):
        sum += roman_hash.get(c)
      else:
        sum -= roman_hash.get(c)
      prev_char = c
    return sum
