n = int(input())

for i in range(n):
  result = f'{" "*(n-i-1)}{"*"*(i+1)}'
  print(result)