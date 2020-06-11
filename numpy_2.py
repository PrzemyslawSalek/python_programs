import numpy as np

tab = np.arange(1, 26).reshape(5, 5)
print(tab)

#wiersze
print(np.fliplr(tab))
#kolumny
print(np.flipud(tab))
#wszystko
print(np.flip(tab))