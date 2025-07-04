def subarraySum(nums, k):
    ct_num_arr = 0
    sum_freq = {0: 1}
    curr_sum = 0
    diff = 0
    for num in nums:
        curr_sum+= num
        diff = curr_sum - k
        if diff in sum_freq:
            ct_num_arr+=sum_freq[diff]
        if curr_sum in sum_freq:
            sum_freq[curr_sum]+=1
        else:
            sum_freq[curr_sum] = 1
    return ct_num_arr


print(subarraySum([1,1,1], 2))

print(subarraySum([-1,-1,1], 0))







