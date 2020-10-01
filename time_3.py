#Zadanie 3
#Zdefiniuj funkcję 'fun_count' odliczającą od zera
#do pewnej dużej, losowej liczby, która na końcu zwraca
#tę liczbę (funkcja powinna działać kilka sekund).
#Następnie napisz program, który:
#• uruchamia 10 wątków z tą funkcją,
#• liczba (wynik) zwracana przez funkcje z każdego
#wątku jest umieszczana w kolejce (obiekt Queue),
#• po zakończeniu wszystkich wątków program pobiera
#wyniki z kolejki i drukuje je na ekranie.

import random
import threading
from queue import Queue

def fun_count():
    num = random.randint(100000, 10000000)
    tmp = 0
    for i in range(0, num):
        tmp += i
    return num

#utworzenie kolejki
que = Queue(maxsize = 10)
print(que.qsize())

t = []
for i in range(0,10):
    print("Wątek {} zaczęty!".format(i))
    t.append(threading.Thread(target=lambda q: q.put(fun_count()), args=(que,)))
    t[i].start()

for i in range(0,10):
    print("Czekamy na koniec wątka {}!".format(i))
    t[i].join()

for i in range(0,10):
    print(que.get(), end=" ")

