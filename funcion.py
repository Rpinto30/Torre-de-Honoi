#Cuando el movimiento actual es impar se mueve el disco 1
#Cuando el movimiento actual es par se mueve el disco que sea igual a la cantidad de veces que hay que dividir el movimiento actual para que sea impar (como me costó esto x'd)
#Para las letras, hago una matriz en vez de una por cada palo, solo voy a marcar la posición de cada disco
#           para n = 4 [Pos Disco 1, Pos Disco 2, Pos Disco 3, Pos Disco 4], si es 0 está en A, 1 en B y 2 en C, todo debe estar en 2
#Los discos se mueven de manera circular

def torre_hanoi(n, i=0, w=None, pos=None):
    total = 2**n - 1
    if w is None:
        if n % 2: w = ['A', 'C', 'B']  #Impar
        else: w = ['A', 'B', 'C'] #par
        pos = [0]*n #linea de la cantidad de discos que hay (n elementos)
    if i == total//2: #Luego de la mitad
        if n % 2: w = ['B', 'C', 'A']  
        else: w =  ['B', 'A', 'C'] 
        
    if i >= total:
        print("Torre resuelta") #ya ta
        return

    m = i + 1 #digamos que el movimiento actual (como el contador pero no en 0)
    disco = 1 #el número del número impar anterior  
    while m % 2 == 0:
        m //= 2 #para que se salga
        disco += 1

    disc_pos = pos[disco-1] # donde está este disco? 0,1,2?
    if disco % 2 == 1: letra = (disc_pos + 1) % 3 #Impar comienza en el 1 (B) 
    else: letra = (disc_pos + 2) % 3 #Par comienza en el 2 (C) 
    print(f"{i+1}) Mover {disco} a {w[letra]}")
    pos[disco-1] = letra #actualizar las posiciones para la otra iteración
    torre_hanoi(n, i+1, w, pos)

# Prueba
while True:
    print ('Bienvenido a la torre de HANOI\n'
           '1. Empezar juego\n'
           '2. Salir')
    select = input('Ingrese una de las opciones: ')
    match select:
        case '1':
            try:
                n = input("Cuantos discos deseas? ")
                print("------------------------")
                torre_hanoi(int(n))
            except ValueError: print("Tiene que ser un número!!")
        case '2':
            break

