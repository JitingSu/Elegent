# 对于数组A[0,1，...，n-1]，请构建一个B数组满足：B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1],不能使用除法
A = []
B = []
n = int(input())
for i in range(0, n):
    A.append(int(input()))
# print(A)
for j in range(0, n):
    temp = 0
    res = 1
    for k in range(0, n):
        if j == k:
            temp = A[k]
            A[k] = 1
            res *= A[k]
            A[k] = temp
        else:
            res *= A[k]
    B.append(res)

print(B)
