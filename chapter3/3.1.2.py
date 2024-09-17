N = int(input())
LIMIT = int(N**0.5)
answer = []

for i in range(2, LIMIT):
    while N % i == 0:
        N //= i
        answer.append(i)

if N != 1:
    answer.append(N)

print(*answer)

