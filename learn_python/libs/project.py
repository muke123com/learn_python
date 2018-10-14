import random
import math
class Project:
    def __init__(self):
        pass

    def selectList(self):

        gameData = {
            1: {
                'name': 'The Witcher 3',
                'description': 'Witchers are mutants, men subjected to gruelling training and flesh-altering experiments that prepare them for one purpose: to kill monsters. Geralt was forged at the elite School of the Wolf and is considered one of the deadliest witchers ever trained. He possesses superhuman reflexes and strength, and his sword fighting skills are second to none.'
            },
            2: {
                'name': 'GTA',
                'description': '《侠盗猎车手5》（Grand Theft Auto V），是由Rockstar Games游戏公司出版发行的一款围绕犯罪为主题的开放式动作冒险游戏。本作于2013年9月17日登陆Play Station 3、Xbox 360平台，2014年11月18日登陆Play Station 4和Xbox ONE平台。多人模式《侠盗猎车手Online》于2013年10月1日正式开放。PC版本已于2015年4月14日推出 [1]  。'
            },
            3: {
                'name': 'Watch Dog 2',
                'description': '《侠盗猎车手5》（Grand Theft Auto V），是由Rockstar Games游戏公司出版发行的一款围绕犯罪为主题的开放式动作冒险游戏。本作于2013年9月17日登陆Play Station 3、Xbox 360平台，2014年11月18日登陆Play Station 4和Xbox ONE平台。多人模式《侠盗猎车手Online》于2013年10月1日正式开放。PC版本已于2015年4月14日推出 [1]  。'
            },
            4: {
                'name': 'Devic May Cry 4',
                'description': '《鬼泣4》是由日本CAPCOM开发的一款动作冒险游戏，是《鬼泣》系列的第四部作品，于2008年1月31日发行。该游戏的故事发生在《鬼泣1》和《鬼泣2》之间，玩家将跟随主角尼禄经历冒险并揭露教皇的阴谋。'
            },
            5: {
                'name': 'Street Fighter 5',
                'description': '《街头霸王5》是卡普空（Capcom）等公司使用虚幻4引擎开发制作研发的3D格斗游戏。该作于2016年2月16日正式发售，登陆PlayStation 4平台和PC平台'
            }
        }
        def showList():
            print('==========================')
            print('1.The Witcher 3')
            print('2.GTA')
            print('3.Watch Dog 2')
            print('4.Devic May Cry 4')
            print('5.Street Fighter 5')
            print('==========================')

            gameNum = input('请选择：')
            return gameNum
            pass
        gameNum = int(showList())
        if(gameNum not in gameData.keys()):
            print('请重新选择')
            self.selectList()
            return
        game = gameData[int(gameNum)]

        print('==========================')
        print(game['name'])
        print(game['description'])
        print('==========================')

        back = input('按1返回上一级')
        if(back == '1'):
            print(back)
            self.selectList()

        pass
    # 百钱白鸡
    def calc1(self):
        cocks = 0
        times = 0
        while(cocks < 20):
            hens = 0
            while(hens < 33):
                chicken = 100 - cocks - hens
                if(5*cocks + 3*hens + int(chicken/3) == 100 and chicken%3 == 0):
                    print('cocks', cocks, 'hens', hens, 'chicken', chicken)
                hens += 1
            cocks += 1
        pass
    # π
    def calcPI(self):
        n = 6
        N = 100000
        d1 = 0.5  # 边长一半
        rad = 360/n/2
        while(n < N):
            d2 = 1 - math.sqrt(1 - d1**2)   # 下一个多边形多出三角形的高
            d1 = 0.5*math.sqrt(d1**2 + d2**2)  # 下一个多边形边长一半
            n *= 2
        # 周长2πr r为1
        l = 2*d1*n  # 多边形周长
        pi = l/2
        print(pi)
        pass