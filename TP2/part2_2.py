from collections import Counter

if __name__ == '__main__':
    ficher = open('input_part2', 'r')
    content = ficher.read()

    tableau = [x for x in content.split('\n')]

    mdp_valide = 0
    frequence = 0
    nb_lettre = 0

    for i in tableau :
        nb_min = i.split('-')[0]
        nb_max = i.split('-')[1].split(" ")[0]
        lettre = i.split(' ')[1].split(":")[0]
        mdp = i.split(' ')[2]
        frequence=mdp.count(lettre)
        nb_lettre = frequence

        #if test2[int(nb_min)-1] == lettre and test2[int(nb_max)-1] != lettre:
         #   mdp_valide = mdp_valide + 1
        if (mdp[int(nb_min) - 1] == lettre and mdp[int(nb_max) - 1] != lettre) or (mdp[int(nb_min) - 1] != lettre and mdp[int(nb_max) - 1] == lettre):
            mdp_valide = mdp_valide + 1

            print(mdp[int(nb_min) - 1])
            print(lettre)
            print(mdp_valide)
