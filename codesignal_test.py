# def division(x,y):
#     return x//y;
# x= 15; y =-4
# data=division(x,y)
# print(data)

def solution(n):
    print(str(n).isnumeric())
    if str(n).isnumeric():
        return n % 2
    else:
        return -1

res=solution(15)

print(res)

