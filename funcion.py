def torre_hanoi(n, i=0, j=1, k=3, w=['A','B','C']):
    text = ''
    if i >= (2**n) - 1:
        print("Torre resuelta")
        return
    else:
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
    print(i, text)


# Prueba
torre_hanoi(3)
