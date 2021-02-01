#https://practice.geeksforgeeks.org/problems/adding-two-matrices3512/1/?track=dsa-workshop-1-matrix&batchId=308#

def sumMatrix(A, B,n1,n2,m1,m2):
    # code here

    #print(len(A))
    c = []
    if n1 == n2 and m1 == m2:

        for i in range(n1):
            row = []
            for j in range(m1):
                row.append(A[i][j] + B[i][j])
            c.append(row)

    return c



