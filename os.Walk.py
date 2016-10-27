import  os

"""
Hatırlarsanız önceki sayfalarda os modülü içindeki listdir() adlı bir fonksiyondan söz
etmiştik. Bu fonksiyon, bir dizinin içeriğini listeleme imkanı veriyordu bize. Mesela o anda
içinde bulunduğumuz dizinde hangi dosya ve alt dizinlerin olduğunu öğrenmek için şöyle bir
komut kullanabiliyorduk:

>>> os.listdir('.')

['build.py', 'gtk', 'kitap', 'make.bat', 'Makefile',
'meta_conf.py', 'py2', 'py3', 'theme', 'tk2', '__pycache__']

Gördüğünüz gibi bu fonksiyon yalnızca kendisine parametre olarak verilen dizinin içeriğini
listeliyor.
Örneğin yukarıdaki çıktıda görünen gtk, kitap, py2, py3, theme, tk2 ve
__pycache__ birer dizin. Ama listdir() fonksiyonu bu dizinlerin de içine girip buradaki içeriği
listelemeye çalışmıyor.
"""

uzantılar = ['txt', 'doc', 'xls',
             'jpeg', 'pdf', 'zip',
'            mp3', 'ogg', 'jpeg']


şablon1 = ['{}.{}'.format('dosya', i) for i in uzantılar[:4]]
şablon2 = ['resim{}.{}'.format(i, uzantılar[-1]) for i in range(1, 5)]
şablon3 = ['{}.{}'.format('dosya', i) for i in uzantılar[4:]]

dosyalar = [('anadizin', şablon1),
            ('resimler', şablon2),
            ('başkadosyalar', şablon3)]


os.makedirs(os.sep.join([dosya[0] for dosya in dosyalar]))


for dizin, şablon in dosyalar:
    for s in şablon:
        open(os.sep.join([dizin, s]), 'w')

os.chdir(dizin)