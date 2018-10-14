from libs import basic
import requests
def main():
    t1 = basic.Basic()
    # t1.test()
    # t1.nine()

    for i in range(10):
        try:
            print(i/0)
        except Exception as e:
            print(e)

    pass
if __name__ == '__main__':
    main()
    pass