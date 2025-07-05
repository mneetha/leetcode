# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
from collections import Counter


def checkInclusion(s1,s2):
    counter_s1 = Counter(s1)
    for i in range(len(s2)-len(s1)+1):
        s2_substr = s2[i:i+len(s1)]
        counter_s2substr = Counter(s2_substr)
        if counter_s1 == counter_s2substr:
            return True
    return False



# print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
# print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(checkInclusion(s1="adc",s2="dcda"))