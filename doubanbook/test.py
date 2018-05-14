import os
from time import time

os.chdir("/home/guixuan/Documents/py/Python-spyder/doubanbook/doubanbook")
t1 = time()
r = os.system("python3.6 main.py")
t2 = time()
print(r)
print("Using time: ")
print(t2 - t1)
