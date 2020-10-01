#Zadanie 2
#Napisz przykładowy program, który sprawdza, o
#ile i czy korzystanie z wątków przyśpiesza (zrównolegla)
#obliczenia.

import time
import threading

def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print("Próba pierwsza: ")
start_time = time.time()
Fibonacci(30)
Fibonacci(30)
print("Brak wątków. Czas potrzebny", time.time() - start_time)

start_time = time.time()
t1 = threading.Thread(target=Fibonacci, args=(30,))
t2 = threading.Thread(target=Fibonacci, args=(30,))
t1.start()
t2.start()

t1.join()
t2.join()

print("Wątki.       Czas potrzebny", time.time() - start_time)

print("Próba druga: ")
start_time = time.time()
Fibonacci(30)
Fibonacci(30)
Fibonacci(30)
print("Brak wątków. Czas potrzebny", time.time() - start_time)

start_time = time.time()
t1 = threading.Thread(target=Fibonacci, args=(30,))
t2 = threading.Thread(target=Fibonacci, args=(30,))
t3 = threading.Thread(target=Fibonacci, args=(30,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Wątki.       Czas potrzebny", time.time() - start_time)
