from msilib.schema import SelfReg
import random
from typing import Self

class carta:
    def init (self,p,v):
        self.pinta= p
        self.valor= v
    def str__(self):
        return " ".join([self.pinta, self.valor])

pinta=("\u2764", "\u2666", "\u2660", "\u2618")
valor=('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')  

class mazo:
    def init (self):
        self.mazo = []
        for pinta in pinta:
             for valor in valor:
             #Crear carta y agrega a lista   
                self.mazo.append(carta(pinta,valor))

      #Mezclar mazo
    def shuffle(self):         
        random.shuffle(self.mazo) 
        
   
    def darunacarta(self):
       singlecarta=self.mazo.pop()
       return singlecarta

#crear clase Mano

VALUES={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
class mano:

    def init (self,jugador):
      self.mano =[] #jugadores partan de una mano vacia
      self.nombre =jugador #define un nombre del jugador
      self.value=0

    def print_hand(self, isdealer=False):
        print(f'La mano de {self.nombre} es:')
        for i in range(0, len(self.mano)):
            if isdealer and i == 0:
                print('X X')
            else:
                print(self.mano[i])
        showvalue = 'X' if isdealer else self.value
        print(f'El valor actual de la mano es: {showvalue}')
        print('**--------------*X*--------------**\n')

    def add_new_card(self,carta):
        self.mano.append(carta)
        self. value += VALUES[carta.rank]


    
     
  #Crear el mecanica del juego
playernames=[]
def init(self,playernames):
    self.winner=""
    m=mazo()
    mazo.shuffle()

playerhandslist = []
for jugador in playernames:
            # reparte dos cartas a cada jugador
            playerhand = mano
            playerhand.add_new_card(mazo.deal())
            playerhand.add_new_card(mazo.deal())
            playerhandslist.append(playerhand)

        # reparte dos cartas a la casa
dealerhand = mano('Dealer')
dealerhand.add_new_card(mazo.deal())
dealerhand.add_new_card(mazo.deal())

SelfReg.mazo = mazo
Self.dealerhand = dealerhand


def print_curr_state(self):
        print('ESTADO DE LA PARTIDA')
        self.dealerhand.print_hand(True)
        for hand in self.playerhands:
            hand.print_hand()

def print_final_state(self):
        print('ESTADO FINAL DE LA PARTIDA')
        self.dealerhand.print_hand(False)
        for hand in self.playerhands:
            hand.print_hand()



# Crear el menu de juego

def create_user():
    allusers = []
    newusername = ''
    while True:
        newusername = input('Ingrese el nombre del nuevo usuario: ')
        if newusername in allusers:
            print('Ese nombre de usuario ya existe')
        else:
            break
    f = open('users.txt', 'a')
    f.write(newusername + '\n')
    f.close()

    return newusername


def create_user():
    allusers = []
    newusername = ''
    while True:
        newusername = input('Ingrese el nombre del nuevo usuario: ')
        if newusername in allusers:
            print('Ese nombre de usuario ya existe')
        else:
            break
    f = open('users.txt', 'a')
    f.write(newusername + '\n')
    f.close()

    return newusername

def select_user():
    allusers = []
    if len(allusers) == 0:
        print("No hay usuarios disponibles")
        return create_user()
    else:
        print('Digite el número del usuario que desea')
        for i in range(0, len(allusers)):
            print(f'{i+1}- {allusers[i]}')
    selecteduser = int(input('Número de usuario: ')) - 1

    return allusers[selecteduser]

def handle_user_select():
    selectorcreate = int(
        input('Seleccione una opción.\n 1-Seleccionar usuario\n 2-Crear usuario\n'))
    while True:
        if selectorcreate == 1:
            return select_user()
        elif selectorcreate == 2:
            return create_user()
        else:
            selectorcreate = int(
                input('Seleccione una opción.\n 1-Seleccionar usuario\n 2-Crear usuario\n'))


def main():
    username = []
    game = game([username])
    game.print_curr_state()
    
    # Dialogo de continuar
    cont = input('Desea continuar? (Y): ')
    while True:
        if cont == 'Y' or cont == 'y':
            break
        else:
            print(cont)
            cont = input('Digite Y para continuar: ')
   