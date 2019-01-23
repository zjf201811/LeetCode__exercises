class Solution(object):

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        set_deck = set(deck)
        count_list = []
        for i in set_deck:
            k=deck.count(i)
            if k==1:
                return False
            count_list.append(k)

        gcd = 2
        min_count=min(count_list)
        while gcd<=min_count:
            for j in count_list:
                if j%gcd!=0:
                    gcd+=1
                    break
            else:
                return True
        return False

print(Solution().hasGroupsSizeX([1,2,1,2,1,2,3]))