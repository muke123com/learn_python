import pyautogui as pag
import time
class StreetFighter(object):
    def __init__(self):
        print(pag.KEYBOARD_KEYS)
        pass

    def ryn(self):
        pag.PAUSE = 0.1
        time.sleep(3)
        # pag.typewrite('iol')

        # pag.typewrite('sdsat')
        pass

    def s_press(self, keys):
        key_arr = keys.split(",")
        for key in key_arr:
            pag.keyDown(key)
            pag.keyUp(key)
            time.sleep(0.2)
        print(key_arr)
        pass
    pass

if __name__ == '__main__':
    sf = StreetFighter()
    sf.ryn()