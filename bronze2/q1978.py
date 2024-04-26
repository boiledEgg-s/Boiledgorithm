# 1978 소수찾기
# https://www.acmicpc.net/problem/1978

def is_prime(num):
    limit = int(num**(1/2))
    for j in range(2, limit+1):
        if num % j == 0:
            return False
    return True

testcase = int(input())
list = input().split()
total = 0

for i in list:
    num = int(i)
    if num == 1: 
        continue
    elif is_prime(num):
        total += 1
print(total)
    

        
        
    