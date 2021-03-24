

new_record = []

ksiazka =[['Imie', 'Nazwisko', 'Numer', 'Miasto'],
        ['Kamil', 'Gut', '512376543', 'Warszawa'],
        ['Maciek', 'Tyszer', '678543098', 'Gdansk'],
        ['Robert', 'Goluch', '789654123', 'Gliwice'],
        ['Aleksander', 'Kammer', '899009321', 'Myslenice']]



while True:
    new_name = input('Podaj imię: ')
    if not new_name.isalpha():
        print("Imię nie może zawierać liczb! ")
        continue
    new_name.islower()
    new_record.append(new_name.capitalize())
    print(new_record)
    break

while True:
    new_surname = input('Podaj nazwisko: ')
    if not new_surname.isalpha():
        print("Nazwisko nie może zawierać liczb! ")
        continue
    new_surname.islower()
    new_record.append(new_surname.capitalize())
    print(new_record)
    break

while True:
    new_number = input('Podaj numer telefonu: ')
    if not new_number.isdigit():
        print("Numer nie może zawierać liter! ")
        if len(new_number) > 9 or len(new_number) < 9:
            print("Numer musi miec 9 cyfr!")
        continue
    new_record.append(new_number)
    print(new_record)
    break

while True:
    new_city = input('Podaj miasto: ')
    if not new_city.isalpha():
        print("Miasto nie może zawierać liczb! ")
        continue
    new_city.islower()
    new_record.append(new_city.capitalize())
    print(new_record)
    break


ksiazka.append(new_record)
for i in range(len(ksiazka)):
    print(i, ' - '.join(ksiazka[i]))


line_nr = int(input("Który wpis chcesz usunąć, od 1-5:   "))
ksiazka.remove(ksiazka[line_nr])

for i in range(len(ksiazka)):
    print(i, ' - '.join(ksiazka[i]))

