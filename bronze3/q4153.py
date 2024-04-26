# 4153 직각삼각형
# https://www.acmicpc.net/problem/4153

while True:
    testcase = input().split()
    list = []
    for i in testcase:
        list.append(int(i))
    list.sort()
    
    if list[0]==list[1]==list[2]==0:
        break
    if(list[0]*list[0] + list[1]*list[1]) == list[2]*list[2]:
        print('right')
    else:
        print('wrong')
    
    
    
