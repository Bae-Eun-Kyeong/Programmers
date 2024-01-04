li = []

for i in range(9):
  n = int(input())
  li.append(n)

print(max(li))

for i in range(len(li)):
  if li[i] == max(li):
    print(i+1)