from math import sqrt
'''
#№1
a = [2, 4, 9, 16, 25]
b = []
for x in a:
    c = round(sqrt(x), 1)
    b.append(c)
print(b)
'''

'''
#№2
def sqr(k):
    return round(sqrt(k), 1)


print(list(map(sqr, [2, 4, 9, 16, 25])))
'''

'''
#№3
print([round(sqrt(i), 1) for i in [2, 4, 9, 16, 25]])
'''
