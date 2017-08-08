class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map = {}
    for index in range(len(nums)):
      map[str(nums[index])] = index

    for index in range(len(nums)):
      if map.get(str(target - nums[index])) != None and map.get(str(target - nums[index])) != index:
        return sorted([map.get(str(target - nums[index])), index])
    return []

obj = Solution()
print(obj.twoSum([3,2,4], 6))
