#https://app.codesignal.com/arcade/python-arcade/meet-python/pLsMG462nzEh3axHN
def solution(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found =upperBound

    return found


s = [0, 4, 2, 3, 1, 7] ; upperBound = 3
res=solution(s,upperBound)
print('Mex of s is {0}'.format(res))