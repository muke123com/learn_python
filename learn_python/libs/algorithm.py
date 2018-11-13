class Algorithm:
    def __init__(self):
        pass

    # 二分法求平方根
    def squareRootBi(x, epsilon):
        # assert 断言
        assert x >= 0, 'x 必须大于等于0'
        assert epsilon > 0, 'epsilon 必须大于0'
        times = 100
        low = 0
        high = x
        guess = (low + high)/2.0
        ctr = 1
        while abs(guess**2 - x) > epsilon and ctr < times:
            print('low:', low, 'high', high, 'guess', guess)
            if(guess**2 < x):
                low = guess
            else:
                high = guess
            guess = (low + high)/2.0
            ctr += 1
        assert ctr <= times
        print('times', ctr, '结果：', guess)
        return guess
        pass


    # 二分法搜索
    def searchBi(x, num):
        assert x <= num, 'x 必须小于等于num'
        s = range(num)
        low = 0
        high = num
        guess = round((low + high)/2)
        ctr = 1
        while(guess != x):
            print('low', low, 'high', high, 'guess', guess)
            if(guess < x):
                low = guess
            else:
                high = guess
            guess = round((low + high) / 2)
            ctr += 1

        print('times', ctr, 'x', x, 'guess', guess)
        pass


