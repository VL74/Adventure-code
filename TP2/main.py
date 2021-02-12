if __name__ == '__main__':
    ficher = open('input', 'r')
    content = ficher.read()

    test = 0
    nombre1 = 0
    nombre2 = 0
    nombre3 = 0
    tableau = [int(x) for x in content.split('\n')]

    for i  in range(0,200):
        for j  in range (0,200):
            for k in range(0,200):
                test = tableau[i] + tableau[j] + tableau[k]
                if test == 2020:
                    nombre1 = tableau[i]
                    nombre2 = tableau[j]
                    nombre3 = tableau[k]
                k = k+1
            j = j+1
        i = i+1

    print(nombre1)
    print(nombre2)
    print(nombre3)

