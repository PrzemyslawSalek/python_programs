#Zadanie 5
#Napisz funkcję, która oblicza rozkład liczby na czynniki
#pierwsze i zwraca wynik w postaci listy krotek
#[(p1,w1),(p2,w2)...], takich, że n = p1w1 * p2w2*...
#...
#Przykład:
#rozklad(756)
#[(2,2),(3,3), (7,1)]
#Następnie wykorzystaj moduł threading i uruchom
#obliczanie rozkładów dla kilku (5) dużych, wielocyfrowych liczb
#(np. 8133343475). Wykorzystaj moduł queue do 'zbierania'
#wyników. Wykorzystaj obiekt klasy threading.Timer do
#monitorowania (np. co sekundę) postępu obliczeń, a w
#przypadku zakończenia danego wątku do wydruku wyniku.

import threading
import random
from queue import Queue

def fun(n):
    wyn = {}
    k = 2
    while n > 1:
        while n % k == 0:
            if k in wyn:
                wyn[k] += 1
            else:
                wyn[k] = 1
            n = n / k
        k = k + 1
    return [(key, value) for (key, value) in wyn.items()]


que = Queue(maxsize = 10)

t = []
for i in range(0,10):
    num = random.randint(1000000, 1000000000)
    t.append(threading.Thread(target=lambda q, arg1: q.put(fun(arg1)), args=(que, num)))
    t[i].start()

for i in range(0,10):
    t[i].join()
    print(que.get())
