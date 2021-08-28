<<<<<<< HEAD
N = int(input())
num_list1 = list(map(int,input().split()))
M = int(input())
num_list2 = list(map(int,input().split()))

dic = dict()

for i in num_list1:
    if i in dic:
        dic[i] += 1
        
    else:
        dic[i] = 1
        
for i in range(M):
    if num_list2[i] in dic:
        print(dic[num_list2[i]], end = ' ')
    else:
=======
N = int(input())
num_list1 = list(map(int,input().split()))
M = int(input())
num_list2 = list(map(int,input().split()))

dic = dict()

for i in num_list1:
    if i in dic:
        dic[i] += 1
        
    else:
        dic[i] = 1
        
for i in range(M):
    if num_list2[i] in dic:
        print(dic[num_list2[i]], end = ' ')
    else:
>>>>>>> ced9c76e4eebb542aa7f213ffc4a80c4cccf43eb
        print(0, end=' ')