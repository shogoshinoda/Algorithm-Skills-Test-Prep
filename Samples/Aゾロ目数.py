n = int(input())

s = n // 9
b = n % 9

if b == 0:
    s -= 1
    b = 9

ans = ''
for i in range(s+1):
    ans += str(b)


print(int(ans))
