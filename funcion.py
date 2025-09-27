def torre_hanoi(n, i=0, w=None, pos=None):
    total = 2**n - 1
    if w is None:
        if n % 2: w = ['A', 'C', 'B']  #Impar
        else: w = ['A', 'B', 'C'] #par
        pos = [0]*n #linea de 4 números

    if i == total//2: #Luego de la mitad
        if n % 2: w = ['B', 'C', 'A']  
        else: w =  ['B', 'A', 'C'] 
        
    if i >= total:
        print("Torre resuelta") #ya ta
        return

    m = i + 1 #
    d = 1 #para el 1,2,1
    while m % 2 == 0:
        m //= 2
        d += 1
    disk = d

    disc_pos = pos[disk-1]
    if disk % 2 == 1: letra = (disc_pos + 1) % 3 #impares más 1 
    else: letra = (disc_pos + 2) % 3 #pares más 2
    print(f"{i+1}) Mover {disk} a {w[letra]}\t\n{m}, {d}, {pos}")
    pos[disk-1] = letra #actualizar las posiciones para la otra iteración
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

