import os


"""
os modülü üzerinde dir() fonksiyonunu uyguladığınızda, orada path adlı bir niteliğin
olduğunu göreceksiniz. Bu nitelik, kendi içinde pek çok önemli fonksiyon ve başka nitelik
barındırır.

Şimdi bu bölümde os.path adlı bu niteliğin içeriğini inceleyeceğiz.


os.path.abspath()
abspath() fonksiyonu, bir dosyanın tam yolunun ne olduğunu söyler:

>>> os.path.abspath('falanca.txt')






os.path.dirname()

dirname() fonksiyonu, bir dosya yolunun dizin kısmını verir:
>>> os.path.dirname('/home/istihza/Desktop/falanca.txt')
'/home/istihza/Desktop'

Bu fonksiyonu abspath() fonksiyonu ile birlikte kullanabilirsiniz:
>>> os.path.dirname(os.path.abspath('falanca.txt'))
'/home/istihza/Desktop'





os.path.exists()

exists() fonksiyonu bir dosya veya dizinin varolup olmadığını kontrol eder:
>>> os.path.exists('/home/istihza/Desktop/falanca.txt')
Eğer böyle bir dosya varsa yukarıdaki kod True çıktısı, yoksa False çıktısı verir.
os.path.expanduser()
expanduser() fonksiyonu bilgisayardaki kullanıcıya ait dizinin adresini verir:
>>> os.path.expanduser('~')
'C:\\Documents and Settings\\fozgul'
veya:
>>> os.path.expanduser('~')
'/home/istihza'
Bu fonksiyonu kullanarak, Windows’ta belirli bir kullanıcı ismi ve dizini de oluşturabilirsiniz:
>>> os.path.expanduser('~denizege')
'C:\\Documents and Settings\\denizege'





os.path.isdir()

isdir() fonksiyonu, kendisine parametre olarak verilen öğenin bir dizin olup olmadığını
sorgular:
>>> os.path.isdir('/home/istihza')
Eğer parametre bir dizin ise True, eğer bir dosya ise False çıktısı alınır.






os.path.isfile()

isfile() fonksiyonu, kendisine parametre olarak verilen öğenin bir dosya olup olmadığını
sorgular:
>>> os.path.isfile('/home/istihza/falance.txt')
Eğer parametre bir dosya ise True, eğer bir dizin ise False çıktısı alınır.






os.path.join()

join() fonksiyonu, kendisine verilen parametrelerden, ilgili işletim sistemine uygun yol
adresleri oluşturur:

>>> os.path.join('dizin1', 'dizin2', 'dizin3') #Windows
'dizin1\\dizin2\\dizin3'
>>> os.path.join('dizin1', 'dizin2', 'dizin3')
'dizin1/dizin2/dizin3'





os.path.split()

split() fonksiyonu, bir yol adresinin son kısmını baş kısmından ayırır:
>>> os.path.split('/home/istihza/Desktop')
('/home/istihza', 'Desktop')
Bu fonksiyonu kullanarak dosya adlarını dizin adlarından ayırabilirsiniz:
>>> dizin, dosya = os.path.split('/home/istihza/Desktop/falanca.txt')
>>> dizin
'/home/istihza/Desktop'
>>> dosya
'falanca.txt'






os.path.splitext()

splitext() fonksiyonu dosya adı ile uzantısını birbirinden ayırmak için kullanılır:
>>> dosya, uzantı = os.path.splitext('falanca.txt')
>>> dosya
'falanca'
>>> uzantı
'.txt'
Gördüğünüz gibi, kendi içinde pek çok nitelik ve fonksiyon barındıran os.path, kullandığımız
işletim sistemine uygun şekilde dizin işlemleri yapabilmemizi sağlayan son derece faydalı bir
araçtır.

"""