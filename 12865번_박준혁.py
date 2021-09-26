n, k = map(int,input().split())

d = [[0 for i in range(k + 1)] for j in range(n+1)]

for i in range(1, n+1):

    weight, value = map(int,input().split())

    for j in range(1, k+1):

        if j < weight:
            d[i][j] = d[i-1][j]

        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-weight]+value)


print(d[-1][-1])