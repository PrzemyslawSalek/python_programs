#Zadanie 4
#Do zadania 2 dodaj funkcję, która jest
#uruchamiana w oddzielnym wątku co sekundę i drukuje
#liczbę aktywnych wątków (nie korzystamy z modułu
#time i funkcji sleep).

import time
import threading

def printit():
  threading.Timer(1.0, printit).start()
  num_threads = threading.activeCount()
  print("Liczba aktywnych wątków:", num_threads)

def Fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

printit()
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