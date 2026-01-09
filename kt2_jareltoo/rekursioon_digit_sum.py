def digit_sum(n):
    if isinstance(n):
        n = abs(n)

        if (n) < 10:
            return n
        return (n) % 10 + digit_sum(n // 10)

    if isinstance < 0:
        raise ValueError
    if not isinstance:
        raise TypeError('TypeError: Funktsiooni sisend pole int')


def main():
    n = (123)
    print(digit_sum(n))

if __name__ == '__main__':
    main()