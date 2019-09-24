s1 = 'abcdefggg'
s2 = 'gbcdegfgg'

def solve(s1, s2):
    if len(s1) == 0:
        return ""
    elif len(s2) == 0:
        return ""
    else:
        if s1[-1] == s2[-1]:
            return solve(s1[:-1], s2[:-1]) + s1[-1]
        else:
            m = ""
            for i in range(len(s1)):
                for j in range(len(s2)):
                    tmp = solve(s1[:-i], s2[:-j])
                    if len(tmp) > len(m):
                        m = tmp
            return m

print(solve(s1, s2))
