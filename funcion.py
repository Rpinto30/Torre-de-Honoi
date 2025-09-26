def torre_hanoi(n, i = 0, j=1):
    if i >= (2**n)-1: print("Torre resuelta")
    else:
        text = ''
        if j%2 != 0:
            text += 'Mover 1 a'
            torre_hanoi(n,i+1,j+1)
        elif j%2 == 0:
            if j != 4:
                text += 'Mover 2 a'
                torre_hanoi(n,i+1,j+1)
            else:
                text += f'Mover 3 a'
                torre_hanoi(n, i + 1, 1)
        print(text, i,j)

torre_hanoi(3, 0, 1)