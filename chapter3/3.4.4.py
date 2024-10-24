N = int(input())

expected_value = 0
for i in range(1, N + 1):
    expected_value += N / i

print(f"{expected_value:.12f}")
