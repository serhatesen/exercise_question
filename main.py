"""

Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

"""

def perfect_number(number):
    perfectNumber = []
    for i in range(1,number+1):
        if (number % i == 0):
            perfectNumber.append(i)
    perfectNumber.pop()
    total = 0
    for a in perfectNumber:
        total = a + total
    return total == number

for i in range(1,1001):
    if(perfect_number(i)):
        print('Mükemmel Sayı: ',i)

"""

Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) 
dönen bir tane fonksiyon yazın.

"""

def ebob_find(numb1,numb2):
    global ebob
    if numb1 > numb2:
        smallNumb = numb2
    else:
        smallNumb = numb1

    for i in range(1, smallNumb+1):
        if numb1 % i == 0 and numb2 % i == 0:
            ebob = i

    return ebob
ebob1 = 18
ebob2 = 24
ebob_result = ebob_find(ebob1,ebob2)
print("EBOB {0}, {1}, = {2}".format(ebob1,ebob2,ebob_result))

"""

Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) 
dönen bir tane fonksiyon yazın.

"""

def ekok_find(numb1, numb2):
    if numb1 > numb2:
        big_numb = numb1
    else:
        big_numb = numb2

    i = big_numb
    while True:
        if i % numb1 == 0 and i % numb2 == 0:
            ekok = i
            break
        i += big_numb

    return ekok

ekok1 = 12
ekok2 = 18
ekok_result = ekok_find(ekok1, ekok2)
print("EKOK({0}, {1}) = {2}".format(ekok1, ekok2, ekok_result))

"""

Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi

"""
ones = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
tens = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def pronunciation(number):  #65
    first = number // 10    #6
    second = number % 10    #5
    return tens[first] + ' ' + ones[second]
print(pronunciation(65))

"""
1'den 100'e kadar olan sayılardan pisagor üçgeni 
oluşturanları ekrana yazdıran bir fonksiyon yazın.
(a <= 100,b <= 100)
"""

def pisagor():
    for a in range(1,101):
        for b in range(1,101):
            c = (a **2 + b **2) **0.5
            if c.is_integer() and c <= 100:
                print(f"Pisagor üçgeni: {a}, {b}, {int(c)}")

pisagor()