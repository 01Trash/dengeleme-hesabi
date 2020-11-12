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

numbers = input("Virgül ile sayıları gir: ")
print("Girdiğiniz Sayılar: {0}".format(numbers))

numberSS=numbers.split(",")
toplam = 0
for n in numberSS:
   toplam = toplam + float(n)

print("GİRDİĞİNİZ SAYILARIN ORTALMASI:{0:.2f} ".format(toplam / len(numberSS)))
