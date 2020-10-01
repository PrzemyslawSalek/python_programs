#Zadanie 2
#Wygeneruj tablicę 5x5 kolejnych liczb z
#zakresu [1,25], a następnie na jej podstawie
#utwórz tablicę która ma:
#• odwróconą kolejność wierszy,
#• odwróconą kolejność kolumn,
#• odwróconą kolejność wierszy i kolumn (w
#rezultacie odwrócona kolejność elementów).

import numpy as np

tab = np.arange(1, 26).reshape(5, 5)
print(tab)

#wiersze
print(np.fliplr(tab))
#kolumny
print(np.flipud(tab))
#wszystko
print(np.flip(tab))