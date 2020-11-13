# A: Aritmetik Ortalama
# l: Ölçmeler
# m: Ortalama Hata
# t: Mutlak Hata
# r: Olası Hata
# E_mm: [|E|] sayıların aritmetik ortalaması ile farklarının mutlak toplamı
# EE_mm: [|EE|] sayıların kareler toplamı

import math
import statistics
import numpy

numbers = input("Virgül ile sayıları gir: ")
print("Girilen sayılar: {0}".format(numbers))

numberSS=numbers.split(",")
toplam = 0
for l in numberSS:
   toplam = toplam + numpy.longdouble(l)
print("Sayıların aritmetik ortalaması: {0:.7f}".format(toplam / len(numberSS)))

# [|E|] sayıların aritmetik ortalaması ile farklarının mutlak toplamı
A = toplam / len(numberSS)
E_mm = A
E_mm_Numbers = []
for l in numberSS:
   E_mm = (numpy.longdouble(l) - A) * 1000
   print("E:", E_mm)
   E_mm = abs((numpy.longdouble(l) - A) * 1000)
   E_mm_Numbers.append(abs(E_mm))
   E_mm += E_mm
print("[|E|]: {0:.7f}".format(abs(E_mm)))

# [|EE|] sayıların kareler toplamı
EE_mm = A
for l in numberSS:
   EE_mm = (numpy.longdouble(l) - A) * 1000
   print("EE:", EE_mm)
   EE_mm = abs((numpy.longdouble(l) - A) * 1000)
   ###print("###EE_mm:: ", EE_mm)
   EE_mm_2 = EE_mm ** 2
   EE_mm_2 = EE_mm_2 + EE_mm ** 2
   ###print("###EE_mm_2: ", EE_mm_2)
print("[|EE|]: {0:.7f}".format(abs(EE_mm_2)))

# Ortalama hata hesabı (m)
m = (EE_mm_2 / len(numberSS)) ** (1/2)
print("Ortalama hata: ±{0:.7f}".format(m))

# Mutlak hata hesabı (t)
t = E_mm / len(numberSS)
print("Mutlak hata: ±{0:.7f}".format(t))

# Olası hata (medyan) hesabı (r)
r = statistics.median(E_mm_Numbers)
print("Olası hata (Medyan): ±{0:.7f}".format(r))


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

