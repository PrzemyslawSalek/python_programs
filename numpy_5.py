import numpy as np

tab = np.random.randint(7, size=(10, 10))
print(tab)

print("Liczby unikalne: {}".format(np.unique(tab)))

liczbyBOOL = {}
liczby = {}
for x in range(0, 7):
    liczby[x] = 0

for x in range(np.size(tab, 1)):
    for y in range(np.size(tab, 0)):
        liczbyBOOL[tab[x][y]] = True
        liczby[tab[x][y]] += 1

for x in range(0, 7):
    print("Liczb {} jest: {}".format(x, liczby[x]))