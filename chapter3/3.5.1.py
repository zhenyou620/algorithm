import random

N = 10000
answer = 0
for i in ramge(0, N):
    px = random().random()
    py = random.random()
    if (px * px + py * py <= 1):
        answer += 1

print(answer)