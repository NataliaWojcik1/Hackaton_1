
### Wojna karciana:
# - Zasady: https://pl.wikipedia.org/wiki/Wojna_(gra_karciana)
# - Konieczność użycia modułu `random`.
# - Program rozdaje karty i drukuje informacje o przebiegu rozgrywki
# - Pomysły na uproszczenie gry:
#     - zamiast implementowa talię kart, używamy liczb (0, 1, 2 ... 9, 10, 11) dla (2, 3, 4, ... Q, K, A)
#     - aby gra kończyła sie wcześniej, rozdajemy tylko 10 kart
#     - dwa tryby: zdobyte karty dochodzą do "ręki", lub są odkładane i nie wykorzystywane


import random






cards_numbers= [2,3,4,5,6,7,8,9,10,11,12,13,14]
cards_symbols = ['♠', '♣', '♥', '♦']

for i in range(len(cards_numbers)):
    for x in cards_symbols:
        print(i,x)
