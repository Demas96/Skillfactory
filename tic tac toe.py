a = [[' ', '0', '1', '2'],  # Обьявление массива для игры
     ['0', '-', '-', '-'],
     ['1', '-', '-', '-'],
     ['2', '-', '-', '-']]

def out():   # Метод вывода массива
    for i in a:
        print(*i)

def pl(var, player):  # Метод для ввода координаты игрока и изменения массива
    while True:
        ch = list(input(f'{player}, введите координаты без пробела: '))
        if len(ch) != 2:  # Проверка правильности ввода координат
            print('Координата введена неверно')
        elif a[int(ch[1]) + 1][int(ch[0]) + 1] == '-':   # Проверка координаты на занятость
            a[int(ch[1]) + 1][int(ch[0]) + 1] = f'{var}'
            break
        else:
            print('Координата занята')
    out()

def chek_win():  # Метод проверки выигрышной комбинации
    cont = 0
    b = ''
    for i in range(len(a)):  # По горизонтали
        for j in range(len(a) - 1):
            if a[i][j] == a[i][j + 1]:
                cont += 1
                b = a[i][j]
        if cont == 2:
            if b == 'X':
                return 1
            elif b == 'O':
                return 2
        else:
            cont = 0
    for j in range(len(a)):   # По вертикали
        for i in range(len(a) - 1):
            if a[i][j] == a[i + 1][j]:
                cont += 1
                b = a[i][j]
        if cont == 2:
            if b == 'X':
                return 1
            elif b == 'O':
                return 2
        else:
            cont = 0
    if a[1][1] == a[2][2] == a[3][3] or a[3][1] == a[2][2] == a[1][3]:   # По диагоналям
        if a[2][2] == 'X':
            return 1
        elif a[2][2] == 'O':
            return 2



print('Игра "Крестики-нолики"')
out()
while True:
    pl('X', 'Игрок 1')
    win = chek_win()
    if win == 1:
        print('Победил Игрок 1!')
        break
    if len(list(x for x in a if '-' in x)) == 0:   # Проверка на остаток свободных координат
        break
    pl('O', 'Игрок 2')
    win = chek_win()
    if win == 2:
        print('Победил Игрок 2!')
        break


print('Игра окончена!')
