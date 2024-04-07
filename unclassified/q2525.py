# 문제 2525: 오븐 시계
# https://www.acmicpc.net/problem/2525

hr, min = input().split()
time = int(input())

hr = int(hr)
min = int(min)

hr = (hr + (int)((min + time) / 60)) % 24
min = (min + time) % 60

print(f'{hr} {min}')