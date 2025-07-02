def first_missing_pos(nums):
    nums.sort()
    print(nums)
    first_missing_pos = 1
    for num in nums:
        if num == first_missing_pos:
            first_missing_pos+=1
        elif num > first_missing_pos:
            break
    return first_missing_pos

first_missing_pos([5, 2, 3, 4])