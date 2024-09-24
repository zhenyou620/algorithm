N = int(input())
A = list(map(int, input().split()))

one_hundred = 0
two_hundred = 0
three_hundred = 0
four_hundred = 0

for i in range(0, N):
    if A[i] == 100:
        one_hundred+=1
    elif A[i] == 200:
        two_hundred+=1
    elif A[i] == 300:
        three_hundred+=1
    else:
        four_hundred+=1  

print(one_hundred*four_hundred + two_hundred*three_hundred)