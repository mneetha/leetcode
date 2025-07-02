def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n


    # Step 1: Prefix product
    prefix = 1
    for i in range(n):
        print(f'i: {i}')
        print(f'prefix: {prefix}')
        answer[i] = prefix
        print(f'answer[i]: {answer[i]}')
        prefix *= nums[i]

    # Step 2: Suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        print(f'i: {i}')
        print(f'suffix: {suffix}')
        answer[i] *= suffix
        print(f'answer[i]: {answer[i]}')
        suffix *= nums[i]

    return answer

# print(productExceptSelf([1, 2, 3, 4]))
def prd_array_except_self(nums):
    answer = [1] * len(nums)
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    num_len = len(nums)
    for index, r_index in zip(range(1, num_len), range(num_len - 2, -1, -1)):
        prefix[index] = prefix[index - 1] * nums[index - 1]
        suffix[r_index] = suffix[r_index + 1] * nums[r_index + 1]
    for index in range(num_len):
        answer[index] = prefix[index] *suffix[index]
    print(prefix)
    print(suffix)
    print(answer)
    # return answer

prd_array_except_self([5, 2, 3, 4])