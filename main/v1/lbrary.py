def power(base, exponent):
    res = 1
    while exponent > 0:
        if exponent & 1:
            res *= base
        exponent >>= 1
        base *= base
    return res

def mod_power(base, exponent, mod):
    res = 1
    while exponent > 0:
        if exponent & 1:
            res = (res * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return res


