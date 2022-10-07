# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re
import itertools

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

pol1 = read_pol('Pol1.txt')
pol2 = read_pol('Pol2.txt')
print('Первый многочлен =', pol1)
print('Второй многочлен =', pol2)

def tup (poly):
    poly = poly.replace(' = 0', '')
    poly = re.sub('[*]', ' ', poly).split('+')
    poly = [i.split(' ') for i in poly]
    poly = [[x for x in list if x] for list in poly]
    for i in poly:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly = [tuple(int(x) for x in j if x != 'x') for j in poly]
    print(poly)
    return poly

def sum_tup(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

def get_pol(pol):
    var = ['*x**'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x**': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

pol1 = tup(pol1)
pol2 = tup(pol2)
summa = sum_tup(pol1, pol2)
print('Сумма многочленов =', summa)
itog_pol = get_pol(summa)
print('Итоговый многочлен =', itog_pol)

with open('Sum_Poly', 'w') as data:
    data.write(itog_pol)
