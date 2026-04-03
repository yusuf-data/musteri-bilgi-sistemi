isim=input("Adınız Nedir?")
soyisim=input("Soyadınız Nedir?")
siparis=input("İlk Siparişinizin Tutarı Nedir?")
siparis2=input("İkinci Siparişinizin Tutarı Nedir?")
siparis3=input("Üçüncü Siparişinizin Tutarı Nedir?")
kdv = 0.19
kdvli_total = float(siparis) + float(siparis2) + float(siparis3) + (float(siparis) + float(siparis2) + float(siparis3)) * kdv
total = float(siparis) + float(siparis2) + float(siparis3)
print(isim, soyisim, "adlı müşteri", kdvli_total, "TL sipariş vermiştir.")
