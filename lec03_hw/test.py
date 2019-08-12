def is_matching(s):
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return False
    else:
        if s[0] == '(' and s[1] == ')':
            return is_matching(s[2:])
        elif s[0] == '(' and s[-1] == ')':
            return is_matching(s[1:-1])
        else:
            return False

print(is_matching(input()))
