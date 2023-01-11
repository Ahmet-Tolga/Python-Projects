import turtle
pen=turtle.Screen()
pen.setup(width=1000,height=500)
pen.bgcolor("black")
pen.title("pinpon oyunu")

draw=turtle.Turtle()
draw.speed(0)
draw.color("white")
draw.penup()
draw.goto(0,250)
draw.pendown()
draw.right(90)
draw.forward(200)
draw.right(90)
draw.circle(50)
draw.left(90)
draw.penup()
draw.forward(100)
draw.pendown()
draw.forward(200)
draw.hideturtle()

ball=turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
x=ball.xcor()
y=ball.ycor()
a=10
b=10

raket1=turtle.Turtle()
raket1.speed(0)
raket1.penup()
raket1.shape("square")
raket1.shapesize(3,1)
raket1.color("gold")
raket1.goto(-470,0)

raket2=turtle.Turtle()
raket2.speed(0)
raket2.penup()
raket2.shape("square")
raket2.shapesize(3,1)
raket2.color("gold")
raket2.goto(470,0)

puan1=0
puan2=0
yazı1=turtle.Turtle()
yazı1.penup()
yazı1.speed(0)
yazı1.goto(-400,200)
yazı1.color("white")
yazı1.write("puan:{}".format(puan1),font="verdena 15 bold")
yazı1.hideturtle()

yazı2=turtle.Turtle()
yazı2.penup()
yazı2.speed(0)
yazı2.goto(400,200)
yazı2.color("white")
yazı2.write("puan:{}".format(puan2),font="verdena 15 bold")
yazı2.hideturtle()

def f():
    y=raket2.ycor()
    y+=20
    raket2.sety(y)
def g():
    y=raket2.ycor()
    y-=20
    raket2.sety(y)
def h():
    y=raket1.ycor()
    y+=20
    raket1.sety(y)
def k():
    y=raket1.ycor()
    y-=20
    raket1.sety(y)
pen.listen()
pen.onkeypress(f,"Up")
pen.onkeypress(g,"Down")
pen.onkeypress(h,"w")
pen.onkeypress(k,"s")
control=False
control2=False
while True:
    x+=a
    y+=b
    ball.setx(x)
    ball.sety(y)
    if(y>240)or(y<-240):
        b*=(-1)
    if(ball.distance(raket2)<30):
        a*=(-1)
    if(ball.distance(raket1)<30):
        a*=(-1)
    if(ball.xcor()>490)or(ball.xcor()<-490):
        a*=(-1)
    if(x>480):
        control=True
        puan1+=10
    if(x<480):
        control=False
    if (control==True):
        yazı1.clear()
        yazı1.write("puan:{}".format(puan1),font="verdena 15 bold")
    if(x<-480):
        control2=True
        puan2+=10
    if(x>-480):
        control2=False
    if (control2==True):
        yazı2.clear()
        yazı2.write("puan:{}".format(puan2),font="verdena 15 bold")
    pen.update()