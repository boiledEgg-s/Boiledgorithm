# 문제 25304: 영수증
# https://www.acmicpc.net/problem/25304

bill_price = int(input())
item_num = int(input())
sum = 0

for i in range(item_num):
    price, num = input().split()
    sum += int(price) * int(num)

text = ''
if sum == bill_price:
    text = 'Yes'
else:
    text = 'No'

print(text)