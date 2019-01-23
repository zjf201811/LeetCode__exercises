class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """

    def sign(p, q, r):
        # cmp函数比较a，b大小，a<b return -1,a==b return 0,a>b return 1
        return cmp((p.x - r.x) * (q.y - r.y), (p.y - r.y) * (q.x - r.x))

    def drive(hull, r):
        hull.append(r)
        # *hull[-3:]表示尾部三个元素
        while len(hull) >= 3 and sign(*hull[-3:]) < 0:
            hull.pop(-2);
        return hull;

        # lambda表示临时写的一个函数
        points.sort(key=lambda p: (p.x, p.y))
        # reduce（f,list,可以作为计算的初始值）
        lower = reduce(drive, points, [])
        # points[::-1]表示反转list
        upper = reduce(drive, points[::-1], []);
        return list(set(lower + upper))