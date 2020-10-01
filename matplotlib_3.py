#Zadanie 3
#Dla pliku tekstowego sporządzić statystykę
#występowania liter. Przedstawić wynik na
#wykresie słupkowym.

import re
import matplotlib.pyplot as plt

l = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
letters = l.split()
print(letters)

ldic = {}
for x in l:
   ldic[x] = 0

file1 = re.subn(r"\W", "", open("plik.txt", "r").read())[0].lower()

for x in file1:
   if x.isalpha():
      ldic[x] += 1

result = []
for x, y in ldic.items():
   if x.isalpha():
      result.append(y)

print(result)
fig = plt.figure()
plt.bar(letters, result)
plt.show()