'''def convert_to_binary(arv):
    if not isinstance(arv, int):
        raise TypeError(f"Funktsiooni sisend pole `int`, on hoopis:{type(arv)} # -> TypeError: Funktsiooni sisend pole `int`, on hoopis: <class 'str'>")
if
    return (arv(-1)) + convert_to_binary(arv)

if __name__ == "__main__":
    main()'''


    def convert_to_binary(arv, astendaja):

                    if isinstance(arv, int):
                    if isinstance(astendaja, int):
                    if astendaja == 0:
                        return 1
                    if astendaja > 0:
                        return arv * aste(arv, astendaja - 1)

                    if astendaja < 0:  # Neg astendaja
                        return 1 / arv * aste(arv, astendaja + 1)

    if not isinstance(arv, int):
        raise TypeError(f"Funktsiooni sisend pole `int`, on hoopis:{type(arv)}
          


    def main():
        vastus = aste()
        print(vastus)


    if __name__ == '__main__':
        main()
