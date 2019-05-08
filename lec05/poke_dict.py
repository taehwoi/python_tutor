N = 151
pokedex = {}
for i in range(N):
    name, number = input().split()
    pokedex[name] = number


pokemon = input()
print(pokedex[pokemon])
