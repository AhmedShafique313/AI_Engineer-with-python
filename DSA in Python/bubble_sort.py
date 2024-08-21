arr = [5, 8, 2, 9, 7]
n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
print('Sorted array: ', arr)