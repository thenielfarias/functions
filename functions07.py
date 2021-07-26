def fatorial(n, show=False):
    c = n
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
        c -= 1
    return f


print(fatorial(5, show=True))


