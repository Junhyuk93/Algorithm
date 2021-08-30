n = int(input())
list_1 = list(map(int,input().split()))
list_2 = list(map(int,input().split()))
answer = 0
for _ in range(n):
    answer += min(list_1) * max(list_2)
    
    list_1.pop(list_1.index(min(list_1)))
    list_2.pop(list_2.index(max(list_2)))
print(answer)