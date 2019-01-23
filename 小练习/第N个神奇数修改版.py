# Author:ZJF
class Solution:

    def nthMagicalNumber(self, N, A, B):
        def lcm(x, y):
            if x % y == 0 or y % x == 0:
                return max(x, y)
            M = 0
            greater = min(x, y)
            for i in range(1, greater):
                if A % i == 0 and B % i == 0:
                    M = i
            return (A*B)//M

        xmax = (N * max(A,B)+1)
        xmin = 0
        x=(xmax+xmin)//2
        m=lcm(A,B)
        while xmin<xmax:

            x = (xmax+xmin)//2
            print(xmax, xmin, x)
            if (x//A+x//B-x//m)>N:
                xmax=x
            elif (x//A+x//B-x//m)<N:
                xmin=x
            elif (x//A+x//B-x//m)==N:
                return int(max([(x//A)*A,(x//B)*B])%1000000007)
print(Solution().nthMagicalNumber(8,8,8))
# print(Solution().nthMagicalNumber(1,2,3))