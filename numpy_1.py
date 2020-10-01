#Zadanie 1
#Wygeneruj tablicę 10x10 kolejnych liczb z
#zakresu [1,100], a następnie na jej podstawie
#utwórz nową tablicę 4x4 składającą się z jej
#środkowych elementów.

import numpy as np

tab = np.arange(1, 101).reshape(10, 10)
print(tab)

tab = tab[3:7, 3:7].reshape(4, 4)
print(tab)