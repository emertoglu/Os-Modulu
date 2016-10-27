import  os

"""
os modülünün stat() fonksiyonu dosyalar hakkında bilgi almamızı sağlar. Bu fonksiyonu
kullanarak bir dosyanın boyutunu, oluşturulma tarihini, değiştirilme tarihini ve erişilme
tarihini sorgulayabiliriz.
stat() fonksiyonunu şöyle kullanıyoruz:

>>> dosya = os.stat('dosya_adı')
>>> dosya
"""

dosya = os.stat('os.Stat.py')

print(dosya)



"""
t_atime   dosyaya en son erişilme tarihi
st_ctime  dosyanın oluşturulma tarihi (Windows’ta)
st_mtime  dosyanın son değiştirilme tarihi
st_size   dosyanın boyutu
"""