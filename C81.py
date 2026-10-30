list_var=[8,1,50,23,6,1,9,4]
print(list_var)
for i in range(len(list_var)):
    for j in range(len(list_var)-i-1):
        if list_var[j]<list_var[j+1]:
            temp=list_var[j+1]
            list_var[j+1]=list_var[j]
            list_var[j]=temp
print(list_var)