import numpy as np
import matplotlib.pyplot as plt

tab = np.random.randint(7, size=(10, 10))
print(tab)

uniq = np.unique(tab)
print("Liczby unikalne: {}".format(uniq))

liczbyBOOL = {}
liczby = [0, 0, 0, 0, 0, 0, 0]

for x in range(np.size(tab, 1)):
    for y in range(np.size(tab, 0)):
        liczbyBOOL[tab[x][y]] = True
        liczby[tab[x][y]] += 1

for x in range(0, 7):
    print("Liczb {} jest: {}".format(x, liczby[x]))

fig = plt.figure()
plt.bar(uniq, liczby)
plt.show()