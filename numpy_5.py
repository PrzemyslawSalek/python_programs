#Zadanie 5
#Wygeneruj tablicę 10x10 liczb losowych
#całkowitych z zakresu [0,6], a następnie
#wydrukuj:
#• listę elementów unikalnych (tzn. jeśli dany
#element w tablicy wystąpił kilkukrotnie, w tej
#liście pojawia się tylko raz),
#• liczbę ich wystąpień.

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