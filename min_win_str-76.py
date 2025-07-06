# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in
# t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".
from collections import Counter, defaultdict


def minWindow(s, t):
    if not t or not s:
        return ""

    need = Counter(t)
    window = {}
    have, need_count = 0, len(need)
    res = [float("inf"), 0, 0]  # window length, left, right
    l = 0

    for r, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            # update result if smaller window found
            if (r - l + 1) < res[0]:
                res = [r - l + 1, l, r]

            # pop from left
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    _, start, end = res
    return s[start:end + 1] if res[0] != float("inf") else ""

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))
print(minWindow(s = "a", t = "aa"))