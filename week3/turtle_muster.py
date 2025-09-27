import turtle

#joonistab 3 ruutu iga jargmineon suurem ja rohkem pooratud
def joonista_3_ruutu(alg_suurus = 30, kasv = 15, alg_nurk = 10, nurga_kasv = 20, varv = 'red'):
    # valine tsukkel 3 ruutu
    for i in range(3):
        suurus = alg_suurus + i * kasv
        nurk = alg_nurk + i * nurga_kasv
        turtle.setheading(nurk)

        turtle.penup
        turtle.goto(-100, 100)
        turtle.pendown
        turtle.color(varv)

        #sisemine
        for i in range(4):
           turtle.forward(suurus)
           turtle.right(90)


#joonistab 5 kolmnurka
def joonista_5_kolmnurka(alg_suurus = 25, kasv = 15, alg_nurk = 5, nurga_kasv = 10, varv = 'purple'):
    # valine tsukkel 5 kolmnurka
    for i in range(5):
        suurus = alg_suurus + i * kasv
        nurk = alg_nurk + i * nurga_kasv
        turtle.setheading(nurk)  # seab kilpkonna suuna tapselt maaratud nurga juurde

        turtle.penup
        turtle.goto(100, -100)
        turtle.pendown
        turtle.color(varv)


            #sisemine tsukkel joonistab kolm nurka
        for i in range(3):
            turtle.forward(suurus)
            turtle.left(120)

#pohifunktsioon mis maarab kiiruse ja kutsub valja teised funktsioonid
def main():
    turtle.speed(0)
    joonista_3_ruutu()
    joonista_5_kolmnurka()
    turtle.done()
#kutsun valja pohifunktsiooni
if __name__ == '__main__':
    main()




