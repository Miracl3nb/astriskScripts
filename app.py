lst = []

with open('tstest.txt', 'r') as archivo:
    lst1 = []
    lst2 = []
    for linea in archivo:
        lst1.append(linea.split(' '))
        
print(lst)