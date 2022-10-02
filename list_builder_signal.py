#https://app.codesignal.com/arcade/python-arcade/meet-python/ZiezPAoWeaK9ThXvQ

def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        b, *res, c = res
        print ("b  :::::: is {0} ".format(b))
        print("c ::::: is {0} ".format(c))
        print("res :::: is {0}".format(res))
    return res

a = [3, 4, 2, 4, 38, 4, 5, 3, 2]
res=solution(a)
print(res)