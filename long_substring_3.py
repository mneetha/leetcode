# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(s) :
    visited_chars = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in visited_chars:
            visited_chars.remove(s[l])
            l += 1
        visited_chars.add(s[r])
        max_len = max(max_len, r - l + 1)

    return max_len



# lengthOfLongestSubstring("abcabcbb")
# lengthOfLongestSubstring("bbbbb")
# lengthOfLongestSubstring("pwwkew")
# lengthOfLongestSubstring("")
# lengthOfLongestSubstring("au")
lengthOfLongestSubstring("aab")