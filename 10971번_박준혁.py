# TSP 알고리즘

# https://velog.io/@kimdukbae/BOJ-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-Python
import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

VISITED_ALL = (1 << n) - 1
cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
idx = 1


def find_path(last, visited):
    if visited == VISITED_ALL:
        return cities[last][0] or INF  # 마지막 도착 도시에서 출발 도시인 0으로 가야됨.(문제 조건)

    if cache[last][visited] is not None:
        return cache[last][visited]

    tmp = INF
    for city in range(n):
        if visited & (1 << city) == 0 and cities[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[last][city])
    cache[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))