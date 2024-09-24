import turtle

# 亀を作成
star = turtle.Turtle()

# 星の形を描く
for i in range(8):
    star.forward(100)   # 100ピクセル進む
    star.right(144)     # 144度右に曲がる

turtle.done()
