import  os

"""

os.makedirs() ise os.mkdir() fonksiyonunun aksine, varolmayan üst ve alt dizinleri de
oluşturma yeteneğine sahiptir. Örneğin:

>>> os.makedirs('/home/istihza/Desktop/aylar/mayıs/ödeme/')

Bu komut sırasıyla aylar, mayıs ve ödeme adlı dizinleri iç içe oluşturacaktır.

Yani os.makedirs() komutunun ödeme adlı dizini oluşturması için aylar ve mayıs adlı dizinlerin
önceden varolması zorunlu değildir.

"""