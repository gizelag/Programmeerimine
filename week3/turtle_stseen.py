import turtle


def joonista_objekt(x, y, suurus, värv):


    #joonistab lihtsa maja
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    #joonista ruudukujuline sein
    turtle.fillcolor()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(suurus)
        turtle.left(90)
    turtle.end_fill()

    #joonista katus
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.goto(x, y + suurus)
    turtle.goto(x+ suurus/2, y + suurus + suurus/2)
    turtle.goto(x + suurus, y + suurus)
    turtle.goto(x, y + suurus)
    turtle.end_fill()

def main():
    turtle.speed(0)
    turtle.color("blue")

    #3maja eri kohtades, suurustes ja varvides
    joonista_objekt(-200, -100, 100, "red")
    joonista_objekt(0, -50, 150, "blue")
    joonista_objekt(200, -150, 80, "green")

    turtle.done()

if __name__ == '__main__':
    main()





