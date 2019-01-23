# Author:ZJF
class Solution:

    def nthMagicalNumber(self, N, A, B):
        def lcm(x, y):
            greater = max([x, y])
            while True:
                if ((greater % x == 0) and (greater % y == 0)):
                    lcm = greater
                    break
                greater += 1
            return lcm

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
print(Solution().nthMagicalNumber(1000000000,3999,40000))
# print(Solution().nthMagicalNumber(1,2,3))

