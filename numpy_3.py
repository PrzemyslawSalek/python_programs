#Zadanie 3
#Wygeneruj tablicę 10x10 liczb losowych
#całkowitych (funkcja numpy.random.randint) z
#zakresu [0,100], a następnie wyzeruj te
#elementy, które są: <25 lub >75.

import numpy as np

tab = np.random.randint(101, size=(10, 10))
print(tab)

for x in range(np.size(tab, 1)):
    for y in range(np.size(tab, 0)):
        if tab[x][y] < 25 or tab[x][y] > 75:
            tab[x][y] = 0

print(tab)