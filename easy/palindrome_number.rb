# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  str = x.to_s
  half_legnth = str.length / 2
  if str[0..(half_legnth-1)] == str[(-half_legnth)..(-1)].reverse
    return true
  else
    return false
  end
end
