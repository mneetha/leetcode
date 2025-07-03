# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import Counter, defaultdict


def groupAnagrams1(str_lst):
    final_list = []
    for i in range(len(str_lst)):
        new_comp = str_lst[i]
        found_match = False
        for lst in final_list:
            if is_anagram(lst[-1], new_comp):
                lst.append(new_comp)
                found_match = True
                break

        if not found_match:
            final_list.append(create_list(new_comp))
    return final_list
def create_list(str_a):
    l1 = []
    l1.append(str_a)
    return l1

def is_anagram(w1,w2):
    return Counter(w1) == Counter(w2)

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))  # key is sorted letters
        anagrams[key].append(word)

    return list(anagrams.values())

print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(groupAnagrams(['a']))
