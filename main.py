def smallest_gap(s):
    letters_found_dic = {}
    pos = 0
    diff = 999999999999999999999
    value1, value2 = 0, 0
    while pos < len(s):
        if not s[pos] in letters_found_dic:
            letters_found_dic[s[pos]] = [pos]
        else:
            letters_found_dic[s[pos]].append(pos)
        pos += 1
    s_pos = 0
    
    while s_pos < len(letters_found_dic[s[s_pos]]):
        pos = 0
        next_pos = 1
        print(letters_found_dic[s[pos]])
        if len(letters_found_dic[s[pos]])>1:
            if letters_found_dic[s[pos]][next_pos] - letters_found_dic[s[pos]][pos] < diff:
                diff = letters_found_dic[s[pos]][next_pos] - letters_found_dic[s[pos]][pos]
                value1 = letters_found_dic[s[pos]][pos]
                value2 = letters_found_dic[s[pos]][next_pos]
            pos = next_pos
            next_pos += 1
        s_pos += 1
    print(letters_found_dic)
    print(value1, value2)
    return s[value1+1:value2]

if __name__ == "__main__":
    print(smallest_gap("ABCDAC"))
    print('-----')
    print(smallest_gap("racecar"))
    print('-----')
    print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
    print('-----')
    #print(smallest_gap("Hello World"))
    print('-----')
    #print(smallest_gap("The quick brown fox jumps over the lazy dog."))