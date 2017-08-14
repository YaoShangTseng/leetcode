# @param {String} s
# @return {Integer}
def roman_to_int(s)
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
  s.split("").reverse.each do |c|
    if prev_char == ""
      prev_char = c
      sum += roman_hash[c]
      next
    end
    if roman_hash[c] >= roman_hash[prev_char]
      sum += roman_hash[c]
    else
      sum -= roman_hash[c]
    end
    prev_char = c
  end
  sum
end
