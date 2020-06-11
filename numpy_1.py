import numpy as np

tab = np.arange(1, 101).reshape(10, 10)
print(tab)

tab = tab[3:7, 3:7].reshape(4, 4)
print(tab)