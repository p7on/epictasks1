def maximum(x, y):
    if x > y:
        return x
    else:
        return y


x, y = int(input('x: ')), int(input('y: '))
print('maximum:', maximum(x, y))
