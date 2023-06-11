# Title Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums: list[int], target: int):
    newMap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in newMap:
            return print(newMap[difference], i)
        else:
            newMap[nums[i]] = i


twoSum([2, 7, 11, 15], 9)
