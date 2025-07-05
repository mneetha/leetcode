from collections import Counter


def findAnagrams(s, p):
    # Initialize result and dictionary structures
    result = []
    p_count = Counter(p)
    s_count = Counter()
    print(len(p))
    print(s_count)
    # Use sliding window
    for i in range(len(s)):
        # Add current character
        s_count[s[i]] += 1
        print(s_count)
        # Remove character outside the window
        if i >= len(p):
            print(i)
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
            print(s_count)
        # Compare dictionaries, add start index to results if an anagram is found
        if p_count == s_count:
            result.append(i - len(p) + 1)
            print(result)

    return result

print(findAnagrams(s = "cbaebabacd", p = "abc"))
# print(findAnagrams(s = "abab", p = "ab"))
# print(findAnagrams("baa", "aa"))