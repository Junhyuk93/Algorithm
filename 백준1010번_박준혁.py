# math 함수의 factorial 사용
import math

n = int(input())

answer_list = []

for _ in range(n):

    w,e = map(int,input().split())

    answer = math.factorial(e) // (math.factorial(e-w) * math.factorial(w))
    
    print(answer)