# A: Aritmetik Ortalama
# l: Ölçmeler
# m: Ortalama Hata
# t: Mutlak Hata
# r: Olası Hata
# b: Bağıl hata
# E_mm: [|E|] sayıların aritmetik ortalaması ile farklarının mutlak toplamı
# EE_mm: [|EE|] sayıların kareler toplamı

import math
import statistics
import numpy

numbers = input("Arada virgül olacak şekilde sayıları gir: ")
#print("Girilen sayılar: {0}".format(numbers))
print("####################################################")

numberSS=numbers.split(",")
toplam = 0
for l in numberSS:
   toplam = toplam + numpy.longdouble(l)
print("Sayıların aritmetik ortalaması: {0:.7f} m".format(toplam / len(numberSS)))

# [|E|] sayıların aritmetik ortalaması ile farklarının mutlak toplamı
A = toplam / len(numberSS)
E_mm = A
E_mm_Numbers = []
for l in numberSS:
   E_mm = (numpy.longdouble(l) - A) * 1000
   #print("E:", E_mm)
   E_mm = abs((numpy.longdouble(l) - A) * 1000)
   E_mm_Numbers.append(abs(E_mm))
   E_mm += E_mm
#Döngü sonucu oluşan E_mm_Numbers sayılarının toplayalı
toplam_E_mm_Numbers = 0
for f in E_mm_Numbers:
   toplam_E_mm_Numbers = toplam_E_mm_Numbers + numpy.longdouble(f)
print("[|E|]: {0:.7f} mm".format(abs(toplam_E_mm_Numbers)))

# [|EE|] sayıların kareler toplamı
EE_mm = A
EE_mm_2_Numbers = []
for l in numberSS:
   EE_mm = (numpy.longdouble(l) - A) * 1000
   #print("EE:", EE_mm)
   EE_mm = abs((numpy.longdouble(l) - A) * 1000)
   EE_mm_2 = EE_mm ** 2
   EE_mm_2_Numbers.append(abs(EE_mm_2))
   EE_mm_2 = EE_mm_2 + (EE_mm ** 2)
#Döngü sonucu oluşan EE_mm_2_Numbers sayılarının toplamı
toplam_EE_mm_2_Numbers = 0
for g in EE_mm_2_Numbers:
   toplam_EE_mm_2_Numbers = toplam_EE_mm_2_Numbers + numpy.longdouble(g)
print("[|EE|]: {0:.7f} mm".format(abs(toplam_EE_mm_2_Numbers)))

# Ortalama hata hesabı (m)
m = (toplam_EE_mm_2_Numbers / len(numberSS)) ** (0.5)
print("Ortalama hata m0: ±{0:.7f} mm".format(m))

# Mutlak hata hesabı (t)
t = toplam_E_mm_Numbers / len(numberSS)
print("Mutlak hata t: ±{0:.7f} mm".format(t))

# Olası hata (medyan) hesabı (r)
r = statistics.median(E_mm_Numbers)
print("Olası hata (Medyan): ±{0:.7f} mm".format(r))

# Bağıl hata hesabı (b)
b = m / A
print("Bağıl hata: ±{0:.7f} mm".format(b))
