import  os

"""
os modülünün listdir() fonksiyonu, bize bir dizin içindeki dosya ve klasörleri listeleme imkanı verir
"""

dizinListele = os.getcwd() # bulundugumuz dizini bir değişkene atadıkk


print( os.listdir(dizinListele)) # yukarıdaki değişkeni parametre olarak atadık

"""
çıktısı :  ['os.Name.py', 'os.Sep.py', 'os.Chdir.py', 'os.Listdir.py', 'os.Getcwd.py', '.idea']

"""