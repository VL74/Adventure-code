import pygame
from pygame.math import Vector2

if __name__ == '__main__':
    ficher = open('input_day3', 'r')
    content = ficher.read()

    tableau = [x for x in content.split('\n')]

    print(tableau)

    nb_arbres = 0
    pos_skieur = Vector2(0,0)

    for i in tableau :
        pos_skieur.x = pos_skieur.x + 3
        pos_skieur.y = pos_skieur.y + 1
        if pos_skieur.x > 30:
            pos_skieur.x = pos_skieur.x - 30
        if i[int(pos_skieur.x)-1] == "#":
            nb_arbres = nb_arbres + 1
        print(i)

