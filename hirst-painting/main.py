# import colorgram
#
# colors = colorgram.extract('hirst_image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# print()
# print(colors)
import turtle as t
import random



new_colors = [(250, 249, 246), (244, 251, 248), (243, 246, 250), (252, 245, 248), (219, 154, 108), (132, 171, 195),
              (221, 73, 89), (213, 132, 150), (26, 119, 152), (240, 208, 99), (122, 176, 149), (39, 119, 84),
              (20, 164, 203), (139, 86, 63), (218, 85, 78), (134, 81, 99), (175, 185, 215), (162, 209, 170),
              (236, 160, 173), (23, 167, 123), (171, 153, 77), (5, 95, 114), (237, 166, 153), (54, 60, 92),
              (151, 207, 221), (38, 59, 77), (103, 126, 172), (38, 83, 54), (230, 212, 18), (69, 71, 46)]

timy = t.Turtle()
t.colormode(255)
timy.shape('circle')
timy.hideturtle()
timy.color('white')
timy.penup()
x = -200
timy.setpos(-250, x)
timy.speed(0)

for _ in range(10):
    timy.setpos(-170, x)
    timy.speed(0)
    for _ in range(10):
        timy.color(random.choice(new_colors))
        timy.stamp()
        timy.fd(40)
    x += 40
# timy.color('white')





screen = t.Screen()
screen.exitonclick()