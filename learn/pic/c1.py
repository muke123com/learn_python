# import cv2
#
# img_path = r'C:\Users\Administrator\Desktop\isux.png'
# img_bit = cv2.imread(img_path)
#
# K = 32
#
# print(img_bit)

# coding=utf-8
import turtle
import time

# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
turtle.left(170)
turtle.end_fill()

turtle.mainloop()
