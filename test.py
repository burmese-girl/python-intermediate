arr = [4, 6, 1, 8, 2]
len = len(arr)
for i in range(len):
    print(i)
    j = 1
    for j in range(len):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
