    # Author:ZJF
import random
class SC2_player_group():
    def group(self, player_list):
        random.shuffle(player_list)
        n=1
        # for i in range(0, len(player_list), 2):
        #     print("{0} \033[31;1mVS\033[0m  {1}".format(player_list[i],player_list[i+1]) )
        for i in player_list:
            print(n,i)
            n+=1

SC2_player_group().group(["brighter","沉默之剑","笑歌自若#51161",
                          "sOs","东乐西乐","龙魂","好汉饶命",
                          "jinAirsOo","SCV","Quirky#51747",
                          "智商低你就数月亮","HELL","CaSER",
                          "西红柿","隔壁小黄","destory"])

