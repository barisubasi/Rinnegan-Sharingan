from turtle import *
renk=input("color: \n")
hideturtle()
pensize(18)

speed(4)
bgcolor("black")
color(renk)

penup()
left(90)
forward(5)
right(90)
left(180)
forward(750)
pendown()

right(146.3)
forward(600)
right(12)
forward(100)
right(12)
forward(150)
right(18.5)
forward(150)
right(12)
forward(100)
right(12)
forward(622)
right(147.2)

left(33.7)
forward(600)
right(12)
forward(100)
right(12)
forward(150)
right(18.5)
forward(150)
right(12)
forward(100)
right(12)
forward(622)
right(147.2)


speed(100000)

penup()
forward(690)
left(90)
forward(5)
right(90)
pendown()

penup()
pensize(0.5)
color("black")
forward(31)
left(30)
color(renk)
pendown()


pensize(10)

def virgul(n):
    for i in range(20):
        if i==11:
            right(95)
            forward(40/n)
            for a in range(4):
               right(15)
               forward(40/n)
            left(170)
            forward(96/n)
            for i in range(6):
               left(10)
               forward(32/n)
            left(3)
            forward(40/n)
            left(12)
            forward(60/n)
            right(13)
        elif i<12:
            left(15)
            forward(32/n)
        else:
            left(15)
            forward(32/n)

right(120)
#right(180)
color(renk)
for i in range(24):
        
        forward(8)
        left(15)
right(180)
pensize(0.0001)
forward(8)
right(180)
right(90)
forward(2)
color("black")
forward(46)
left(90)
color(renk)
pensize(10)

for i in range(1,25):
    if i==1:
        penup()
        pensize(12)
        forward(10)
        pendown()
        pensize(10)
        forward(11)
        left(15)
     
    elif  i==8  or (i)==7 or (i)==16 or (i)==15 or (i)==24 or i==23:
        penup()
        color("black")
        pensize(12)
        forward(21)
        left(15)
        pensize(10)
        pendown()
    else:
        color(renk)
        forward(21)
        left(15)

    if (i)/8==1 or (i)/8==2 or (i)/8==3:
        color(renk)
        left(108)
        virgul(4)
        right(108)

penup()
color("white")
left(81)
forward(77)
right(27)
forward(10)
right(90)
forward(188)
left(90)
left(180)
forward(25)
left(180)
pendown()




for i in range(1,49):
    if   i==12 or i==13 or (i)==28 or (i)==29 or (i)==44 or i==45  :
        pensize(10)
        forward(10)
        color("black")
        pensize(12)
        forward(15)
        left(7.5)
        pensize(10)
    else:
        color(renk)
        forward(25)
        left(7.5)

    if (i+3)/16==1 or (i+3)/16==2 or (i+3)/16==3:
        color(renk)
        left(120)
        virgul(4)
        right(120)



penup()
color("white")
left(84)
forward(191)
left(90)
forward(20)
left(90)
forward(300)
left(90)
pendown()


for i in range(1,49):
    if   i==5 or (i)==21 or i==37  :
        color("black")
        pensize(10)
        forward(40)
        left(7.5)
        pensize(10)
    else:
        color(renk)
        forward(40)
        left(7.5)

    if (i+11)/16==1 or (i+11)/16==2 or (i+11)/16==3:
        color(renk)
        left(120)
        virgul(4)
        right(120)


penup()
left(264)
forward(85)
right(90)
forward(40)
right(180)
pendown()


for i in range(48): 
    forward(50)
    left(7.5)

penup()
left(86)
forward(380)
right(56)
forward(460)
left(90)
pendown()

for i in range(48): 
    if i<4:
        if i==3:
            forward(40)
            penup()
            forward(20)
            pendown()
            left(7.5)
        else:
            forward(60)
            left(7.5)
    elif i<29 and i>20:
        forward(60)
        left(7.5)
    elif i==29:
        forward(10)
        penup()
        forward(50)
        pendown()
        left(7.5)
    elif i>42:
        forward(60)
        left(7.5)
    else:
        penup()
        forward(60)
        left(7.5)
        pendown()


penup()
right(90)
right(90)
forward(10)
left(90)
forward(80)
left(90)
pendown()

for i in range(48): 
    if i<2:
        forward(70)
        left(7.5)
    elif i==2:
        forward(10)
        penup()
        forward(60)
        pendown()
        left(7.5)
    elif i==22:
        penup()
        forward(30)
        pendown()
        forward(40)
        left(7.5)
    elif i<27 and i>22:
        forward(70)
        left(7.5)
    elif i==27:
        forward(10)
        penup()
        forward(60)
        pendown()
        left(7.5)
    elif i==45:
        penup()
        forward(60)
        pendown()
        forward(10)
        left(7.5)
    elif i>45:
        forward(70)
        left(7.5)
    else:
        penup()
        forward(70)
        left(7.5)
        pendown()


penup()
right(90)
forward(77)
left(90)
pendown()

for i in range(48): 
    if i<1:
        forward(80)
        left(7.5)
    elif i==1:
        forward(10)
        penup()
        forward(70)
        pendown()
        left(7.5)
    elif i==23:
        penup()
        forward(60)
        pendown()
        forward(20)
        left(7.5)
    elif i<26 and i>23:
        forward(80)
        left(7.5)
    elif i==26:
        forward(10)
        penup()
        forward(70)
        pendown()
        left(7.5)
    elif i>46:
        forward(80)
        left(7.5)
    else:
        penup()
        forward(80)
        left(7.5)
        pendown()




hideturtle()
done()

