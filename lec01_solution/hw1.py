"""SIGMA CALCULATOR"""

N, K = input().split()
N = int(N)
K = int(K)
print(sum(range(K+1)) - sum(range(N)))
