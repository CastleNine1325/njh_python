columns = 4
def gugudan():

    for j in range(2, 10, columns):
        for i in range(1, 10):
            for k in range(columns):
                print(f'{(j+k)} x {i} = {(j+k)*i:2d}', end='\t')
            print()
        print()
gugudan()
