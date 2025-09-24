import turtle

def joonista_kolmnurk():"""joonistab punase kolmnurga asukohas -150, 0 ja kasutab for tsukklit"""


    turtle.goto(-150,0)
    turtle.color('red')
    for i in range(3):#kulgede arv 3
        turtle.forward(100)#100 uhikut
        turtle.left(120)#poordenurk 120

def joonista_ruut():"""joonistab sinise ruudu asukohas -50, 0 ja kasutab for tsukklit"""


    turtle.goto(-50,0)
    turtle.color('blue')

    for i in range(4):#4 kulge ja 150 uhikut ja 90kraadi
        turtle.forward(150)
        turtle.left(90)

def joonista_viisnurk():
    """joonistab rohelise viisnurga asukohas 150, 0 kasutab for tsukklit"""

    turtle.goto(150,0)
    turtle.color('green')

    for i in range(5):#5 kulge ja 250 uhikut ja 72kraadi
        turtle.forward(250)
        turtle.left(72)

def main():#pohifunktsioon mis joonistab koik kujundid

    turtle.speed(5)
    joonista_kolmnurk()
    joonista_ruut()
    joonista_viisnurk()
    turtle.done()

if __name__ == '__main__':
    main()