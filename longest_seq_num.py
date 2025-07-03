

def longestConsecutive(nums):
    num_set = set(nums)
    print(num_set)
    current_num = 0
    current_streak = 0
    longest_streak = 0
    for num in num_set:

        if num-1 not in num_set:
            print(f'# Starting a new sequence as `num - 1`({num - 1}) was not present')
            current_num = num
            current_streak = 1


        while current_num + 1  in num_set:
            print(' Increasing the streak as consecutive number is found')
            current_num+=1
            current_streak +=1

        print('Update the maximum streak length if the current streak is longer')
        longest_streak = max(longest_streak, current_streak)

    return longest_streak



longestConsecutive([100,4,200,1,3,2])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])