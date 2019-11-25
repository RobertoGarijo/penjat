# Projecte final de trimestre: Crear el joc del penjat

import random

IMAGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |

=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print('Jugant al PENJAT')

palabras = "Padrastre seguretat ulleres llapis indústria vegetal paraules banc biblioteca planta robot almanac altipla balbucejar terratremol tornado tauro casa assolellat estoig superheroi cascada litoral massacre arxipelag remoli muntanya arqueoleg otorinolaringoleg vesicula aterridor llibre surfer escalador explorador tsunami japones raig santoral catedral passeig cano optica teclat hidraulica boligraf ordinador". split (' ')



index = random.randint(0, len(palabras) - 1)

palabraSecreta = palabras[index]

indexPS = 0

print('La palabra té ' + str(len(palabraSecreta)) + ' lletres. No cal repetir lletres')

print(IMAGENES_AHORCADO[0])

error = 0

lenLletrasTro = 0

lletrestrobades = []
lletresmalvades = []

while error < len(IMAGENES_AHORCADO):
    print('Escriu una lletra')
    lletraS = input()
    indexPS = 0
    encert = False

    if lletraS in lletrestrobades:
        print('No has de repetir lletres!')
        error += 1
        print(IMAGENES_AHORCADO[error])

    else:

        while indexPS < len(palabraSecreta):
            lletra = palabraSecreta[indexPS]
            if (lletraS == lletra):
                print(lletraS, end=' ')
                lletrestrobades.append(lletraS)
                encert = True
            else:
                lenLletrasTro = 0
                trobada = False
                while lenLletrasTro < len(lletrestrobades) and not trobada:

                    if lletra == lletrestrobades[lenLletrasTro]:
                        print(lletra, end=' ')
                        trobada = True

                    lenLletrasTro += 1

                if not trobada:
                    print('_', end=' ')

            indexPS += 1

        if not encert:

            print(IMAGENES_AHORCADO[error])
            print('lletra ' + lletraS + ' no es troba a la paraula')
            if lletraS in lletresmalvades:
                print('Aquesta lletra ja la has posada!')
            else:
                lletresmalvades.append(lletraS)
            error += 1

            print ('Les lletres ' + str(lletresmalvades) + ' no son a la paraula')

    if error == len(IMAGENES_AHORCADO) - 1:
        print('Has perdut')
        print ('La paraula era ' + (palabraSecreta))
        break
    if len(lletrestrobades) == len(palabraSecreta):
        print('Has guanyat!!!!!!!!!1!!!!!!!!!!!!!!!')
        break
    print("Errors: " + str(error))
