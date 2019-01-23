# Author:ZJF
class Solution:
    def nthMagicalNumber(self, N, A, B):
        def gcb(p, q):
            if p == q:
                return p
            if p < q:
                return gcb(q, p)
            else:
                if p & 1:
                    if q & 1:
                        return gcb(p - q, q)
                    else:
                        return gcb(p, q >> 1)
                else:
                    if q & 1:
                        return gcb(p >> 1, q)
                    else:
                        return gcb(p >> 1, q >> 1) << 1
        C = gcb(A, B)
        if C == A or C == B:
            return C * N % 1000000007
        if A > B:
            A, B = B, A
        D = A * (B // C)
        a, b = D // A, D // B
        m, n = N // (a + b - 1), N % (a + b - 1)
        y = int(n / (a / b + 1))
        x = int(a / b * y)
        nowA, nowB = A * x, B * y
        while x + y < n:
            if nowA + A < nowB + B:
                nowA += A
                x += 1
            else:
                nowB += B
                y += 1
        return (max(nowA, nowB) + m * D) % 1000000007
print(Solution().nthMagicalNumber(1000000000,39999,40000))