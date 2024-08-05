N = int(input())
num_list = list(map(int, input().split()))

a = 0
for i in range(N):
    a = a + num_list[i]

print(a%100)