"""
author:Nebularr
version 1.1
BUG修复，流程和显示优化
石头剪刀布游戏：
石头（1）/剪刀（2）/布（3）
电脑随机出拳，用户从键盘输入，石头胜剪刀，剪刀胜布，布胜石头
"""
import random
print("**********石头剪刀布GAME************")
print("author:Nebularr \nversion 1.1 ")
print("****本游戏使用积分制，获胜积1分，平局不积分****\n获胜条件：积分值先到5者获胜")
dict_player ={"石头":1,"剪刀":2,"布":3}
dict_computer={1:"石头",2:"剪刀",3:"布"}
while 1:
    player_score=0
    computer_score=0
    while 1:
        if player_score < 5 and computer_score < 5:
            temp = input("请输入您要出的拳:石头/剪刀/布:\n")
            if temp in dict_player:
                player = dict_player[temp]
                computer = random.randint(1, 3)

                print("您出的拳头是 %s - 电脑出的拳头是 %s" %(temp,dict_computer[computer]))

                if ((player == 1 and computer == 2)
                        or(player == 2 and computer == 3)
                        or(player == 3 and computer == 1)):
                    player_score += 1
                    # print("恭喜你，赢了,电脑弱爆了！")
                elif player == computer:
                    pass
                    # print("真是旗鼓相当的对手呀！再来一盘吧！")
                else:
                    computer_score+=1
                    # print("你输了弟弟，电脑碉堡了！")
                print("当前积分:电脑 %d分- 玩家 %d分"%(computer_score,player_score))
            else:
                print("请输入正确的值！Try again.")
        elif player_score == 5:
            print("Victory!恭喜你获得本局游戏的总胜利！")
            break
        elif computer_score == 5:
            print("Defeat!别气馁，再尝试一次叭！")
            break
