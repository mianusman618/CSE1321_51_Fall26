user_input=input("Enter Comma Sep Numbers : ")
k=int(input("Enter Rot Count : "))

org_list=user_input.split(",")
#print(org_list)
list_nums=[]
for i in range(len(org_list)):
    list_nums.append(int(org_list[i]))
print("List of Numbs : ",list_nums)
#[40,50,10,20,30]
k=k%len(list_nums)
for i in range(k):
    last_element=list_nums[len(list_nums)-1]
    for j in range(len(list_nums)-1,0,-1):
        list_nums[j]=list_nums[j-1]
    list_nums[0]=last_element
print("Rotated ",list_nums)
