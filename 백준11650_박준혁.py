import sys # readline 써야 통과
n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    n_list.append([x,y])
    
n_list.sort()

for i in range(n):
    print(" ".join([str(_) for _ in n_list[i]]))