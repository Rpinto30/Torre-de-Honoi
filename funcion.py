def torre_hanoi(n, i = 0, j=1, k = 3):
    if i >= (2**n)-1: print("Torre resuelta")
    else:
        text = ''
        if j%2 != 0:
            text += 'Mover 1 a'
            torre_hanoi(n,i+1,j+1, k)
        elif j%2 == 0:
            if j != 4:
                text += 'Mover 2 a'
                torre_hanoi(n,i+1,j+1, k)
            else:
                text += f'Mover {k} a'
                if k == n: torre_hanoi(n, i + 1, 1, 3)
                else: torre_hanoi(n, i + 1, 1, k+1)
        print(text, i,j, k)

torre_hanoi(4)