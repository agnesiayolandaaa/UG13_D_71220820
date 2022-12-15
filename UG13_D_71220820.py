import turtle

# buat turtle
t=turtle.Turtle()
sc= turtle.Screen().bgcolor("purple")

t.color("white")
t.pensize(10)
t.up()
t.goto(-50,-10)
t.down()


# menggambar huruf A
t.left(90)
t.right(20)
t.forward(100)
t.right(140)
t.forward(100)
t.backward(50)
t.right(110)
t.forward(30)




sc=turtle.Screen().exitonclick()