# @param {Integer} x
# @return {Integer}
def reverse(x)
  x_to_string = x.to_s
  if x_to_string[0] == '-'
    answer = (x_to_string[0] + x_to_string[1..-1].reverse).to_i
  else
    answer = (x_to_string[0..-1].reverse).to_i
  end

  if ( answer > 2 ** 31 - 1) || ( answer < -1 * 2 ** 31 )
    return 0
  else
    return answer
  end
end
