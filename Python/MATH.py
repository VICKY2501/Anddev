from sympy import *
init_printing(use_unicode=True)

def element(matrix, i, j):
    return list(matrix.row(i).col(j))[0]

def showMatrix(matrix, r, c):
    """ To display Matrix """
    for R in range(r):
        print("[", end = " ")
        for C in range(c):
            var = list(matrix.row(R).col(C))[0]
            print(var, end = " ")
        print("]\n")

def rank(matrix, r, c):
    count = 0
    for i in range(r):
        for j in range(c):
            element = list(matrix.row(i).col(j))[0]
            if element != 0:
                count += 1
                break
    return count

def solvefor_3(mat, r, c):
    """ Solve if rank(A) == rank(Augmented A) """
    if rank(mat, r, c) == rank(mat, r, c - 1):
        x,y,z = symbols('x y z')
        vars = [x, y, z]
        k = 0
        for i in range(r):
            sol = 0
            for j in range(c - 1):
                sol = sol + element(mat, i, j) * vars[j]
            eq1 = Eq(sol, element(mat, i, c - 1))
            vars[k] = solve(eq1)[0]
            k += 1
        return vars
    else: 
        return "None"
             
def consistency(echelonMatrix, r, c):
    p_augmented = rank(echelonMatrix, r, c)
    p_mat = rank(echelonMatrix, r, c - 1)
    
    if p_augmented == p_mat:
        if p_mat == r:
            print("System is CONSISTENCE and has UNIQUE SOLUTION\n")
        elif p_mat < r:
            print("System is CONSISTENCE and has INFINITE SOLUTION\n")
        else:
            print("System is CONSISTENCE\n")
        
    else:
        print("System is INCONSISTENCE\n")
    
def ask(r, c):
    """ return input matrix from user """
    A = Matrix([ [input(f"Enter {j} element of {i} Row = ") for j in range(1, c + 1)] for i in range(1, r + 1) ])
    return A


# DRIVER CODE
r, c = input("ENTER NUMBER OF ROWS & COLUMNS = ").split()
r = int(r)
c = int(c)

# augmented matrix input
A = ask(r, c)

echelonA = A.rref(pivots = False)

print("Echelon Form of A :")
showMatrix(echelonA, r, c)
print(f"Rank = {rank(echelonA, r, c)}\n")
print(f"SOLUTION = {solvefor_3(echelonA, r, c)}\n")
consistency(echelonA, r, c)
