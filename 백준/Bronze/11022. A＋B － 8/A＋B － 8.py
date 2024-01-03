t = int(input())

for i in range(t):
  a, b = map(int, input().split())
  result = f'Case #{i+1}: {a} + {b} = {a+b}'
  print(result)