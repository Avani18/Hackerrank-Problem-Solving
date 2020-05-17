
def compareTriplets(a, b):

    arr = [0, 0]
    for i in range(3):
        if (a[i] > b[i]):
            arr[0] += 1
        elif (a[i] < b[i]):
            arr[1] += 1
    return arr

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(' '.join(map(str, result)))
