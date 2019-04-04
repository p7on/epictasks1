x, y = int(input()), int(input())


def maximum(x, y):
    if x > y:
        return(x)
    elif y > x:
        return(y)
    else:
        return('try one more time')

print(maximum(x, y))
