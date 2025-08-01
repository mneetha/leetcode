from typing import List


def countBits(n: int)-> List[int]:
    ans = [0]* (n+1)
    for i in range(len(ans)):
        ans[i] = bin(i)[2:].count('1')
    return ans

print(countBits(5))