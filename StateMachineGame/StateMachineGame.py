from enum import Enum, auto, unique
from random import randint
import time


class States(Enum):
    atacando = auto()
    defendendo = auto()
    recuperando = auto()
    intangivel = auto()
    morto = auto()
    default = auto()

class GameObject:
    def __init__(self):
        self.__state = States.default

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Entity (GameObject):
    def __init__(self):
        super().__init__()
        self.__health = 100
    def dano(self, dano):
        #dano normal aplicado
        self.__health -= dano
        if(randint(0,9) == 1):
            #dano critico aplicado se validado
            self.__health -= dano
            print("CRITICAL STRIKE! DANO x2")
            print("")
    def dano_def(self, dano2):
        self.__health -= (dano2/2)
    def set_health(self):
        curaTotal = randint(5,15)
        self.__health += curaTotal
        print(curaTotal, " de vida recuperada")
        print("vida atual", self.get_health())
        print("")
        if(randint(0,9) == 1):
            self.__health += randint(5,10)
            print("Cura bonificada!")
            print("")
    def get_health(self):
        return self.__health


player = Entity()
enemy = Entity()
contador = 10
rodada = 1
while True:
    if player.get_state() == States.default:
        enemy.set_state(States.atacando)
        if rodada%4 == 0:
            enemy.set_state(States.recuperando)
        print("|-------------------------------------------------------------------------|")
        print("|  escreva exatamente seu próximo modo!                                   |")
        print("|  Ex: 1                                                                  |")
        print("|  atacar lhe faz dar um dano aleatório de 5 a 15                         |")
        print("|  defender te fazlevar metade do dano do inimigo                         |")
        print("|  Recuperar te faz recuperar de 5 a 15 de vida. sujeito a Bônus!         |")
        print("|  1 > atacando | 2  > defendendo | 3 > recuperando | 4 > intangivel      |")
        print("|-------------------------------------------------------------------------|")
        modo = input("insira aqui: ")
        print(modo)
        if modo == "1":
            player.set_state(States.atacando)
        elif modo == "2":
            player.set_state(States.defendendo)
        elif modo == "3":
            player.set_state(States.recuperando)

        else:
            print("valor errado, tente novamente")
            pass
        pass
    if player.get_state() == States.atacando:
        player.set_state(States.default)
        dmg = randint(5,15)
        enemy.dano(dmg)
        print("Dano deferido: ", dmg,)
        print("vida atual do inimigo: ", enemy.get_health())
        print("")
        if enemy.get_health() <= 0:
            print("voce venceu!")
            break
    if player.get_state() == States.recuperando:
        player.set_state(States.default)
        print("Jogador recupernado vida")
        player.set_health()

    if enemy.get_state() == States.atacando and player.get_state() != States.defendendo and player.get_state() != States.intangivel:
        player.set_state(States.default)
        dmg = randint(5, 20)
        player.dano(dmg)
        print("Dano sofrido: ", dmg)
        print("vida atual: ", player.get_health())
        print("")
        if player.get_health() <= 0:
            print("voce perdeu!")
            break

    if enemy.get_state() == States.atacando and player.get_state() == States.defendendo and player.get_state() != States.intangivel:
        player.set_state(States.default)
        dmg = randint(5, 20)
        player.dano_def(dmg)
        print("Dano sofrido: ", dmg)
        print("vida atual: ", player.get_health())
        print("")
        if player.get_health() <= 0:
            print("voce perdeu!")
            break

    if enemy.get_state() == States.recuperando:
        player.set_state(States.default)
        print("Inimigo recupernado vida")
        print("")
        enemy.set_health()





    time.sleep(1)
    rodada += 1
    print()
    print("-------------------------------------------------------------------")
    print()




