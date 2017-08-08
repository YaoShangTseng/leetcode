# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  map = {}
  nums.each_with_index do |i_value, i_index|
    map[i_value] = i_index
  end
  # map = { 3: 0, 4: 1, 2: 2}

  nums.each_with_index do |i_value, i_index|
    if map[target - i_value] && map[target - i_value] != i_index
      return [map[target - i_value], i_index].sort
    end
  end
  return []
end
