def reverseWords(s):
    word_list = s.split()
    left_idx = 0
    right_idx = len(word_list)-1
    while left_idx != right_idx and left_idx < right_idx:
        word_list[left_idx], word_list[right_idx] = word_list[right_idx], word_list[left_idx]
        left_idx+=1
        right_idx-=1
    return " ".join(word_list)

print(reverseWords('  hello world  '))