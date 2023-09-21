import turtle


screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.shape("turtle")
t.color("brown")
t.speed(0)




def dibujar_f1(t, radio):
    t.pensize(2)  
    t.pencolor("black")  
    t.color("yellow")
    t.begin_fill()
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("brown")  
    t.pensize(1)


def dibujar_f2(t, radio):##añaden esta nueva funcion para la flor izq
    t.penup()
    t.goto(-200,60)
    t.pensize(2)  
    t.pencolor("black")  
    t.color("yellow")
    t.begin_fill()    
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("brown")  
    t.pensize(1)




def dibujar_f3(t, radio):##añaden esta nueva funcion para la otra flor de la derecha
    t.penup()
    t.goto(200,60)
    t.pensize(2)  
    t.pencolor("black")  
    t.color("yellow")
    t.begin_fill()
    t.circle(radio, 60)
    t.left(120)
    t.circle(radio, 60)
    t.end_fill()
    t.pencolor("brown")  
    t.pensize(1)
    


def dibujar_girasol():
    radio = 80    
    
    t.penup()
    t.goto(0, -100) 
    t.pendown()
    t.pensize(8) 
    t.left(90) 
    t.color("green")
    t.forward(180)  
    
    
    for _ in range(18):
        dibujar_f1(t, radio)
        t.left(20)
    t.penup()
    t.goto(-200, -100) 
    t.pendown()
    t.pensize(8) 
    t.left(360) 
    t.color("green")
    t.forward(180)


    t.penup()
    t.goto(13, 80) 
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    for _ in range(18):
        dibujar_f2(t, radio)
        t.left(20)
    t.penup()
    t.goto(200, -100) 
    t.pendown()
    t.pensize(8) 
    t.left(360) 
    t.color("green")
    t.forward(180)


    t.penup()
    t.goto(-187, 60) 
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(15)
    t.end_fill()


    for _ in range(18):
        dibujar_f3(t, radio)
        t.left(20)
    
    t.penup()
    t.goto(218, 60)  
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(16)
    t.end_fill()


t.penup()
t.goto(-400, -100)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(800)  
    t.right(90)
    t.forward(200) 
    t.right(90)
t.end_fill()




dibujar_girasol()


t.penup()
t.goto(0, 200)
t.color("red")
t.write("aqui va el texto", align="center", font=("arial", 20, "bold"))


t.hideturtle()
turtle.done()






#mbcehm#
