N = 151
pokedex = [0] * 151
for i in range(N):
    pokedex[i] = input().split()


pokemon = input()
for p in pokedex:
    if p[0] == pokemon:
        print(p[1])
        break
