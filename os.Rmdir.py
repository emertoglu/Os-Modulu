import  os

"""
os modülünün rmdir() fonksiyonu, içi boş bir dizini silmek için kullanılır:
>>> os.rmdir('dizin_adı')
"""



"""
>>> os.makedirs('anadizin/dizin1/dizin2/dizin3/dizin4')

Anadizin altındayken şu komutlar hata verecektir:


>>> os.rmdir('anadizin')
>>> os.rmdir(r'anadizin/dizin1')
>>> os.rmdir(r'anadizin/dizin1/dizin2/dizin3')


Çünkü bu dizinlerinin hiçbirinin içi boş değil; her birinin içinde birer dizin var. Ama şu komut
başarılı olacaktır:


>>> os.rmdir(r'anadizin/dizin1/dizin2/dizin3/dizin4')

"""
