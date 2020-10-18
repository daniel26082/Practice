import turtle as trtl

# draw left curve 90 degrees
trtl.pendown()
for i in range(6):
  trtl.forward(10)
  trtl.left(15)
trtl.penup()

def draw_y_axis():
  trtl.goto(0,0)
  trtl.pendown()
  trtl.forward(100)
  trtl.backward(200)
  trtl.penup()

def draw_x_axis():
  trtl.goto(0,0)
  trtl.left(90)
  trtl.pendown()
  trtl.forward(100)
  trtl.backward(200)
  trtl.penup()

draw_y_axis()
draw_x_axis()