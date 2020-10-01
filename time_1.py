#Zadanie 1
#Korzystając z modułu time wydrukuj na ekranie:
#• aktualny czas analogiczny do postaci: 'Dzisiaj jest
#środa, 3 czerwiec 2020 roku, godzina 13 minut 50.'
#• liczbę godzin, jaka upłynęła między 11 marca 2020 a
#3 czerwca 2020,
#• jaki był dzień tygodnia 16 października 1978

import time, datetime

#aktualny czas analogiczny do postaci: 'Dzisiaj jest
#środa, 3 czerwiec 2020 roku, godzina 13 minut 50.'

print(time.strftime("Dzisiaj jest %A, %d %b %Y roku, godzina %H minut %M.", time.gmtime()))

#liczbę godzin, jaka upłynęła między 11 marca 2020 a
#3 czerwca 2020,

first_date = '03 06 2020'
second_date = '11 03 2020'
print((datetime.datetime.strptime(first_date, '%d %m %Y')-datetime.datetime.strptime(second_date, '%d %m %Y')).days*24)

#jaki był dzień tygodnia 16 października 1978

date = '16 10 1978'
days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
print(days[datetime.datetime.strptime(date, '%d %m %Y').weekday()])

