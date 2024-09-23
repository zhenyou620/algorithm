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
    
R = GCD(A[0], A[1])
for i in range(2, N):
    R = GCD(R, A[i])

print(R)