s = "У лукоморья 123 дуб зеленый 456"
if s.find('я'):
    print('index:', s.index('я'))
print('y appers in the text {n} times'.format(n=s.count('у')))
if not s.isalpha():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print('О' + s[1:])

'''
или через списки:
s.list()
s[1] = 'О'
"".join(s)
'''
