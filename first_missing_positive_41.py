def first_missing_pos(nums):
    #sort method
    # nums.sort()
    # print(nums)
    # first_missing_pos = 1
    # for num in nums:
    #     if num == first_missing_pos:
    #         first_missing_pos+=1
    #     elif num > first_missing_pos:
    #         break
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap numbers to their correct position.
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # If after rearrangement, nums[i] != i + 1, i + 1 is the missing number.
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all numbers are in their correct positions, the missing number is n+1
    return n + 1
    # return first_missing_pos

print(first_missing_pos([1, 10, 2]))