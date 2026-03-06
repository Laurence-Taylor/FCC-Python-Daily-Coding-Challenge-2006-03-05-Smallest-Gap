def smallest_gap(s):
    letters_found_dic = {}
    pos = 0
    while pos < len(s):
        if not s[pos] in letters_found_dic:
            pass 
        pos += 1
    return s

if __name__ == "__main__":
    print(smallest_gap("ABCDAC"))
    print('-----')
    print(smallest_gap("racecar"))
    print('-----')
    print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
    print('-----')
    print(smallest_gap("Hello World"))
    print('-----')
    print(smallest_gap("The quick brown fox jumps over the lazy dog."))