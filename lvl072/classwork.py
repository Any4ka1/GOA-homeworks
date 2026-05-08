def fact(num):
    if len(num) == 0:
        return 1
    return num[0] * fact(num[1:])
print(fact([1, 2, 3, 4, 5]))


def factorio(girlidk):
    if girlidk == 0:
        return 1
    return girlidk * factorio(girlidk - 1)
print(factorio(5))