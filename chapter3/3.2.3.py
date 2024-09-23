N=int(input())
A=list(map(int, input().split()))

def GCD(A,B):
    while A > 0 and B > 0:
        if A >= B:
            A = A % B
        else:
            B = B % A
    if A <= 0:
        return B
    return A

def LCM(A, B):
    return int(A*B/GCD(A,B))

R = LCM(A[0], A[1])
for i in range(2, N):
    R = LCM(R, A[i])

print(R)

