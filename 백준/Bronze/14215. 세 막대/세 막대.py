a,b,c = map(int, input().split())

# 모두 더한합 - 가장 큰값 <= 가장큰값  : 나머지 두 값 합한게 가장 큰거보다 작음 => 삼각형 성립 x
if [a,b,c].count(a) == 3 :
    print(sum([a,b,c]))
elif sum([a,b,c]) - max([a,b,c]) <= max([a,b,c]):
    mx = sum([a,b,c]) - max([a,b,c]) - 1
    print(sum([a,b,c])-max([a,b,c]) +mx)
else :
    print(sum([a,b,c]))