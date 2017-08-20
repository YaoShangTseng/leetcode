# @param {String} s
# @return {Boolean}
def is_valid(s)
  arr = []
  s.split('').each do |c|
    if arr.length == 0
      arr.push c
      next
    end
    case c
    when ')'
      if arr.last == '('
        arr.pop
      else
        arr.push c
      end
    when ']'
      if arr.last == '['
        arr.pop
      else
        arr.push c
      end
    when '}'
      if arr.last == '{'
        arr.pop
      else
        arr.push c
      end
    else
      arr.push c
    end
  end
  arr.length == 0
end
