s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

s = s.split()

for x in range(len(s) - 1):
    if s[x][0] == 'м' or s[x][0] == 'М':
        del s[x]

a = ' '.join(s)
print(a)
