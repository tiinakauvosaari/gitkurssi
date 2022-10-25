for n in range(2, 10):
    for x in range(2, n):
        if ((n % x) == 0):
            print(n, "on yhtä kuin", x, "*", int(n/x))
            break
    else: # Huomaa, että tämä else on jälkimmäiselle forille!
 # Kierros päättyi siten, että ohjelma ei löytänyt sopivaa paria
        print(n, "on alkuluku")
