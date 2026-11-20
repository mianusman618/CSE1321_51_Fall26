rows=int(input("Enter No of Rows : "))
cols=int(input("Enter No of Columns : "))
#matrx=[[1,2,3,4],[5,6,7,8]]
matrix=[]
num=1
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(num)
        num+=1
    matrix.append(row)
print("matrix :")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()

border_elem=[]
sum_bord=0
inner_sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
       if i==0 or i==rows-1 or j==0 or j==cols-1:
           border_elem.append(matrix[i][j])
           sum_bord+=matrix[i][j]
       else:
           inner_sum+=matrix[i][j]
print("Border elements : ",border_elem)
print("Sum of Border elems : ",sum_bord)
print("Sum of inner elems : ",inner_sum)

