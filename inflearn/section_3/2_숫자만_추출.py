import sys
input = sys.stdin.readline

msg = input().replace('\n','')
new = []
count = 0
for x in msg:
    if x.isdigit():
        new.append(x)
new = int(''.join(new))

for i in range(1,new+1):
    if new % i == 0:
        count += 1

print(new)
print(count)
