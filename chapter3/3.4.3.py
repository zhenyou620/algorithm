N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
for i in range(N):
    answer += A[i] / 3 + 2 * B[i] / 3

print("%.12f" % answer)
 