def torre_hanoi(n, i=0, j=1, k=3, w=['A','B','C']):
    text = ''
    if i < (2**n) - 1:
        if j % 2 != 0:
            text += f"Mover 1 a {w[(i % 2) + 1]}"
            if j == 4:
                torre_hanoi(n, i+1, j+1, k+1, w)
            else:
                torre_hanoi(n, i+1, j+1, k, w)
        elif j % 2 == 0:
            if j != 4:
                text += f"Mover 2 a {w[(i % 3)]}"
                torre_hanoi(n, i+1, j+1, k, w)
            else:
                if i != (2**n - 1)//2:
                    text += f"Mover {k} a {w[(i//k) % 3]}"
                    if k == n-1:
                        torre_hanoi(n, i+1, 1, 3, w)
                    else:
                        torre_hanoi(n, i+1, 1, k+1, w)
                else:
                    text = f"Mover {n} a C"
                    torre_hanoi(n, i+1, 1, 3, w)
        print(f"{i+1}) "+text  )
    else:
        print("Torre resuelta")

print("LEER DE ABAJO PARA ARRIBA")

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
            except: print("Tiene que ser un número!!")

        case '2':
            break

