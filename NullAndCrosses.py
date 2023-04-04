import random

def PrintMatrix(matrix):
    print("")
    text = " " + " | ".join([str(i) for i in matrix[0:3]])
    print(text.replace(" 0 ", "\033[1;31m 0\33[0m").replace(" X ", "\033[1;32m X \33[0m"))
    print("---|---|---")
    text = " " + " | ".join([str(i) for i in matrix[3:6]])
    print(text.replace(" 0 ", "\033[1;31m 0\33[0m").replace(" X ", "\033[1;32m X \33[0m"))
    print("---|---|---")
    text = " " + " | ".join([str(i) for i in matrix[6:9]])
    print(text.replace(" 0 ", "\033[1;31m 0\33[0m").replace(" X ", "\033[1;32m X \33[0m"))
    print("---|---|---")
    print("")

def Check(matrix):
    if (matrix[0] == matrix[1] == matrix[2] or
        matrix[3] == matrix[4] == matrix[5] or
        matrix[6] == matrix[7] == matrix[8] or
        matrix[0] == matrix[3] == matrix[6] or
        matrix[1] == matrix[4] == matrix[7] or
        matrix[2] == matrix[5] == matrix[8] or
        matrix[0] == matrix[4] == matrix[8] or
        matrix[2] == matrix[4] == matrix[6]): return True
    return False

matrix = [1,2,3,4,5,6,7,8,9]
PrintMatrix(matrix)

end = False
while(end == False):
    try:
        InputNum = int(input("Your turn --->  "))
        if(InputNum>0) & (InputNum<10) & (matrix[InputNum-1] not in [" 0 ", " X "]):
            matrix[InputNum-1] = " X "
            PrintMatrix(matrix)
            if Check(matrix):
                print('You won!')
                ened = True
            elif len(set(matrix)) == 2:
                print("Try more!")
                end = True
            else: 
                InputNum = random.choice([i for i in matrix if i not in [" 0 ", " X "]])
                print("AI TURN ------>", InputNum)
                matrix[InputNum-1] = " 0 "
                PrintMatrix(matrix)
                if Check(matrix):
                    print("AI won!")
                    end = True
            # break
        else:
            print("Error")
    except: True





        