def is_subseq(s, t):
    len_t = len(t)
    len_s = len(s)
    s_i = 0
    if s_i == len_s:
        return True
    for t_i in range(len_t):
        if t[t_i] == s[s_i]:
            s_i += 1
        if s_i == len_s:
            return True
    return s_i == len_s

print(is_subseq('axc', 'ahbgdc'))