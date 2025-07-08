# Given an integer array nums, find the subarray with the largest sum, and return its sum.

from collections import Counter, defaultdict


def maxSubArray(nums):
    max_sum = nums[0]  # Start with the first element as the initial max
    current_sum = nums[0]  # Start with the first element in the running sum

    # Start iterating from the second element
    for i in range(1, len(nums)):
        # If current_sum is improved by starting a new subarray at i, reset current_sum
        current_sum = max(nums[i], current_sum + nums[i])
        # Update max_sum to be the maximum encountered sum so far
        max_sum = max(max_sum, current_sum)

    return max_sum

print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray(nums=[1]))
print(maxSubArray(nums = [5,4,-1,7,8]))

