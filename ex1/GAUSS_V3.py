A = [
    [1, 2, 3],#, 8],  # 0 0 = 1     0 1 = 2     0 2 = 3
    [4, 5, 6],#, 9], 
    [7, 8, 9]#,17]#,  ## 1 0 = 4     1 1 = 5    1 1 = 6
   # [7, 8, 9, ]  # 2 0 = 7    2 1 = 8   2 2 = 9
]

b = [1, 1, 1]#, 1]


# 1 - умножение на чиселку
# 2 - перестановка
# 3 - сложение
# 1) и 3)
# 4 - вывод на экран

def umnozhit(Matrix, Free, str, number, n):#кстати, в питоне можно использовать русские слова в т.ч. как название функций. хотя я считаю, что стоит не полениться и погуглить, что умножение в англицком именуется multiplication и вообще, что есть какие-то стандарты языка типо pep 8
    Matrix[str] = [Matrix[str][j] * number for j in range(n)]
    Free[str] *= number


def perestanovka(Matrix, Free, str1, str2):
    Matrix[str1], Matrix[str2] = (Matrix[str2], Matrix[str1])
    Free[str1], Free[str2] = (Free[str2], Free[str1])

def slozhenie(Matrix, Free, str1, str2, n):
    Matrix[str1] = [Matrix[str1][j] + Matrix[str2][j] for j in range(n)]
    Free[str1] += Free[str2]


def sloz_umnoz(Matrix, Free, str1, str2, number, n):#странная функция имхо
    Matrix[str1] = [Matrix[str1][j] + number * Matrix[str2][j] for j in range(n)]
    Free[str1] += number * Free[str2]


def printM(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()


def printF(Free):
    for i in range(len(Free)):
        print(Free[i], end=' ')
        print()

#дальше мне было лень читать)
def Gauss(Matrix, Free):
    str = 0
    while (str < len(Free)):
        stl_max = -1
        for r in range(len(Matrix)):
            if (Matrix[str][r] != 0):
                stl_max = r
        if (stl_max == -1):
            print("No solutions")
        # return 0

        umnozhit(Matrix, Free, str, 1 / Matrix[str][stl_max], len(Matrix))

        for r in range(len(Matrix)):
            if(r!=str):
                sloz_umnoz(Matrix, Free, r, str, -1 * Matrix[r][stl_max], len(Matrix))

        if (stl_max != str):
            perestanovka(Matrix, Free, stl_max, str)

        str = str + 1


#printM(A)


Gauss(A, b)

k=0
for r in range(len(A)):
   if(A[r]==[0,0,0]):
       k=k+1
    
rg = len(A) - k 





print("================rg================")
print(rg)

print("================A================")
printM(A)
print("================b================")
printF(b)

N = len(A)
M = len(A) - rg
F = [[0] * M for i in range(N)]

for i in range(N - rg):
    for j in range (M):
        if (i == j):
            F[i][j] = 1
        else:
            F[i][j] = 0
            

for i in range(N - rg,N):
    for j in range (M):
        F[i][j] = - A[i][j]

print("================F================")
printM(F)   


