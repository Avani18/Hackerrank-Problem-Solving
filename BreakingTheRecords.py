
def breakingRecords(scores):

    mini = scores[0]
    maxi = scores[0]
    maxc = 0
    minc = 0
    for i in range(1, len(scores)):
        if (scores[i] > maxi):
            maxi = scores[i]
            maxc += 1
        elif (scores[i] < mini):
            mini = scores[i]
            minc += 1

    return maxc, minc


if __name__ == '__main__':

    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
	print (result)
