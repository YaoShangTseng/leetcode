# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return '' if strs.length == 0
  return strs.first if strs.length == 1

  temp = strs.first
  strs.each do |str|
    temp.split('').each_with_index do |v, i|
      if str[i] == v
        next
      else
        if i == 0
          return ''
        else
          temp = str[0..(i-1)]
          break
        end
      end
    end
  end
  temp
end
