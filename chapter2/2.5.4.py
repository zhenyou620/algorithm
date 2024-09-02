N = int(input())
answer =[]

for i in range(2, N+1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        answer.append(i)

print(*answer)