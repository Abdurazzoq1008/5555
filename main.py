def maxSon(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "Barchasi teng!"

a=10
b=10
c=10

kataSon = maxSon(a,b,c)

print("Kata son: ", kataSon)

