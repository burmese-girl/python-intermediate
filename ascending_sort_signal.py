def solution(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        print('i is {0}  '.format(i))
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

arr = [2, 4, 1, 5]
res = solution(arr)
print('Result is : {0}'.format(res))