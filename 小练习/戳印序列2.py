
# Author:ZJF
class Solution:
    def is_coincide(self, list1, list2):
        if "".join(list1).isdigit():
            return False
        else:
            for (m, n) in zip(list1, list2):  # 切出来的和印章匹配
                if m != n and m != "0":
                    return False
            else:
                return True
    def movesToStamp(self, stamp, target):
        count = 0
        add_count = 0
        number_list = []
        m = len(stamp)
        n = len(target)
        stamp_list = list(stamp)
        target_list = list(target)
        while True:
            if "".join(target_list).isdigit():
                number_list.reverse()
                print(count)
                return number_list
            if count > add_count:
                print(count)
                return[]
            else:
                count += 1
            for i in range(n-m+1):   # 补全印章
                the_list = target_list[i:i + m]
                if self.is_coincide(the_list, stamp_list):
                    number_list.append(i)
                    add_count+=1
                    target_list[i:i+m]=["0"]*m


print(Solution().movesToStamp("dca", "ddcaddcaaa"))
print(Solution().movesToStamp("abc", "abc"))
print(Solution().movesToStamp("abc", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))
print(Solution().movesToStamp("dcba","dcbababdcdcbaacbadcdcbdcbadcdcbaabaacdcdcdcbabadcbabacbddcbadcbadcbacbadcbabdcbdcdcbabdddcbaadcbaabdcbdcdcbabdcbaaddcbdcbadcbadcbaaadcbdcbadcbabacbabaddcbaadcbaacbddcbabacbdcbacbadcbaddcbdcbacbaadcdcbadcbaaadcbaddcdcbacdcbabddcbdcdcbadcdcbacbddcbaabababadcbadcbaabaabadcbabaadcbdcbacbabadcbababdcddcbabadcdcbacbadcbadcbabdcbddcbabaaddcdcbabdcbaaddcbdcbaddcbacbababdcdcbadcbacddcbabacbadcbadcbaacdcbaabacbaaadcdcdcbaaadcbadcbacbdcbaadcbacbaddcdcbadcbaababaddcbaababadcdcbababdcbadcbacbabdcbadcbabaadcbdcbabdcbaaadcbadcbadcddcbdcbabacbaadcdcbabaddcdcbacdcdcbaababdcdcbababaacddcbdcdcbacbadcbadcbabdcbaacdcbdcbaaddcdcbaddcbadcdcdcbaaadcbaacdcbacdcbabadcdcbdcbaadcbdcdcbabacbdcbababacbadcdcbacdcbdcbacbadcbadcdcbaadcbabadcbdcbabadddcbabaadcbaadcbaaaabaaddddcbadcbdcbacbadcbadddcddcbaaacbaadcbabadcdcbadcbadcbdddcbacbaddcbacbabaaacdddcbadcbdcbadcdcbaadcbabaddcbabadcbadcbadcbabdcbabadcbdcbaadcbacbadcbdcbacbacbdcbaacdcbadcdcbacbadcbadcbacdcbabadcbdcdcbacbacdcbabadcbaabaddcdcbabadcbadcbaadcbabaabddcbaaaaa"))
print(Solution().movesToStamp("zgadeocmortwzxd",
"zgazgadeocmortwzxdezgadeocmortwzxdocmortwzxdtwzxdrtwzxdzgadeocmortwzxdmozzgadeocmortwzxdwzxdoczgadeocmortwzgadeocmortwzxdmortwzxdzgadeoczzgadeocmortwzxdgzgadeocmortwzxdtwzxdgazgadeocmortwzgadeocmortwzxdcmortwzxdxdzgadeoczgadeocmortwzxdeocmzgazgadezgzgzgadeocmortwzxdocmortwzxdortwzxdzgzgadeocmortzgadeocmortwzxdgadeocmortwzxddcmorzgadeozgadeocmortzgadeocmorzgadeocmortwzxdgadeocmortzgadeocmortwzxdxdrtwzzgazgzgadeocmortwzxddzgadzgadeocmortwzxdwzxdeozzgazgzgadeocmortwzxdxdtwzxdgadeocmortwzxdadeocmozgadeocmortwzxddeocmorzgadeocmortwzxdzgadeocmortwzxdocmortwzxdzgazgadeocmortwzxddeocmzgadeocmortwzxdcmortwzxzgadeocmortzgadeocmortwzxdrtwzxdzgadeocmortwzzgadzgadeocmortwzxdzgadeoczgadzgadezgadeocmortwzxdzgadeocmortwzxdmortzgadeocmorzgadeocmortwzxdeocmozgadeocmortwzxdwzxdwzxdocmortwzxdeocmzgadeocmortwzxdocmortwzxdmortwzxdeozgadeocmortwzxdadeocmortwzgadeocmortwzxddeocmortwzxdeocmozgadeocmortwzxdgazgazgadeocmartwzxdmortwzxdeocmozgadeocmortwzxdzxdortwzzgadeocmortwzxdxdadzgadeocmortwzxdzgadeocmortwzxdd"))