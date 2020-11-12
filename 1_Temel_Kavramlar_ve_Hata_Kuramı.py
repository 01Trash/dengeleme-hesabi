# A: Aritmetik Ortalama
# m: Ortalama Hata
# t: Mutlak Hata
# r: Olası Hata
# E_mm: |E| Sayıların aritmetik ortalaması ile farklarının mutlak toplamı
# EE_mm: |EE| kareler toplamı

# Kütüphane;
import math

numbers = input("Virgül ile sayıları gir: ")
print("Girilen sayılar: {0}".format(numbers))

numberSS=numbers.split(",")
toplam = 0
for n in numberSS:
   toplam = toplam + float(n)
print("Sayıların aritmetik ortalaması:{0:.2f} ".format(toplam / len(numberSS)))

# Sayıların aritmetik ortalaması ile farklarının mutlak toplamı hesabı
A = toplam / len(numberSS)
E_mm = A
for n in numberSS:
   E_mm = float(n) - A
   print("E:", E_mm)
   E_mm += E_mm
print("[|E|]: ", abs(E_mm))

EE_mm = A
for n in numberSS:
   EE_mm = float(n) - A
   print("E:", EE_mm)
   EE_mm += EE_mm ** 2
print("[|EE|]: ", abs(EE_mm))



# n: Ölçü sayısı
# u: Bilinmeyen sayısı
# d: Datum efekt
# f: Kesin değer
"""
f = n - u + d
Fazla ölçü sayısı veya serbestlik derecesi olmak üzere kesin değerin hesabı;
f > 0 ise dengeleme ile yapılır.
f = 0 ise cebrik çözüm ile yapılır (Ölçme problemidir.).
f < 0 ise sonsuz sayıda çözüm ile yapılır.
"""
# L: Ölçü
# N: Gerçek değer
# X: Kesin değer
# E: Hata
# V: Düzeltme
"""
E = N - L
V = X - L
"""
# Mutlak hata (Ei) = Ölçü (Li) - Gerçek değer (N)
"""Mutlak Ortalama Hata

"""

