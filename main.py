import turtle
import turtle as tur

tur.bgcolor('black')
fred = turtle.Turtle()
fred.pensize(4)
fred.color('green')
fred.left(90)
fred.backward(100)
fred.speed(200)

def gambarpohon(i):
    if i<10:
        print('Inside if')
        return
    else:
        print('Inside else')
        fred.forward(i)
        fred.color('yellow')
        fred.circle(2)
        fred.color('brown')
        fred.left(30)
        gambarpohon(3 * i / 4)
        fred.right(60)
        gambarpohon(3 * i / 4)
        fred.left(30)
        fred.backward(i)

gambarpohon(100)

#Created By CodersB3rdasi
tur.color('red')
tur.penup()
tur.goto(0,-165)
tur.write('Created By:', align='center', font="papyrus 13 bold")
tur.color('white')
tur.goto(0,-200)
tur.write('CodersB3rdasi', align='center', font="papyrus 20 bold")

tur.done()



