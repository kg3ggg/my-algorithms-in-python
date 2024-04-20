
def search_gsd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print(search_gsd(21, 35))
