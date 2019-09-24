"""369"""
n = input()
ret = ["SAFE", "CLAP"]
k = 3

mlt_of_k = (int(n) % k == 0)
contains_k = str(k) in n

print(ret[mlt_of_k or contains_k])
