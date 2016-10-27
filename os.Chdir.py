import os

"""
os modülünün chdir() fonksiyonu bize bir dizinden başka bir dizine geçme imkanı verir.
"""

print(os.getcwd())

print("+"*50)

os.chdir("/home/aspa")    # home aspa dizinine geçiş yaptık  

print("+"*50)

print(os.getcwd())

