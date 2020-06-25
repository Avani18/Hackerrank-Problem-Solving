
def diagonalDifference(arr):
    n = len(arr)
    pd = 0
    sd = 0
    for i in range(0,n):
        pd += arr[i][i]  
        sd += arr[i][n-i-1]
    return (abs(pd-sd))

if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print (result)
