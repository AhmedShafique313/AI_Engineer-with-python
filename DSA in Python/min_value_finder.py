num = int(input('How you long the array: '))
arr = []
for i in range(num):
    n = int(input('Enter the value: '))
    arr.append(n)

min_val = arr[0]
for e in arr:
    if e < min_val:
        min_val = i
    
print('Lowest value index: ', min_val)
print('Sorted list: ', arr)