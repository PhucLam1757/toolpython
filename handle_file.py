from os import path
import openpyxl


with open("handle3.txt") as f:
    a = f.read()
with open("handle4",'w+') as s:
    s.write(a)  
print(s)      


