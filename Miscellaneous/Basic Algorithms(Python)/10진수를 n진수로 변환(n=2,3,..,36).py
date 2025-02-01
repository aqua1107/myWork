#10진수를 n진수로 변환하기 (n=2,3,...,36)
def converter(x, r):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = ''
    while x>0:
        a += s[x % r]
        x //= r

    return a[::-1]

print(converter(50, 18))