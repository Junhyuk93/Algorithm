N = int(input())

sen_list = []

for _ in range(N):
    sentence = str(input())
    sen_list.append(sentence)

#중복제거
sen_list = list(set(sen_list))

# 사전순 -> 짧은것부터
sen_list.sort()
sen_list.sort(key=len)

while True:
    print(sen_list.pop(0))
    if len(sen_list) == 0:
        break