from typing import List
from collections import Counter

def singleNumber(nums: List[int]) -> List[int]:
    k_counter = Counter(nums)
    # print(k_counter[1])
    ans = [0,0]
    i = 0
    for key,value in k_counter.items():
        if value == 1:
            ans[i] =key
            i+=1
        if i == 2:
            break

    return ans



print(singleNumber([1,2,1,3,2,5]))