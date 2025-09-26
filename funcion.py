def torre_hanoi(n, i = 0, j=1, k = 3):
    text = ''
    if i >= (2**n)-1: print("Torre resuelta")
    else:
        if i < n//2:  w = ['A', 'C', 'B']
        else:  w = ['B', 'A', 'C']
        if j%2 != 0:
            text += 'Mover 1 a'
            if j==4: torre_hanoi(n,i+1,j+1, k+1)
            else:torre_hanoi(n,i+1,j+1, k)

        elif j%2 == 0:
            if j != 4:
                text += 'Mover 2 a'
                torre_hanoi(n,i+1,j+1, k)
            else:
                if i != ( (2**n)-1)//2:
                    text += f'Mover {k} a'
                    if k == n-1:
                        torre_hanoi(n, i + 1, 1, 3)
                    else:
                        torre_hanoi(n, i + 1, 1, k+1)
                else:
                    text = f'Mover {n} a C'
                    torre_hanoi(n, i + 1, 1, 3)

    print(text)
    #print(i,j,k)
torre_hanoi(5)
print(31//2)