user_input=input("Enter Numbs Comma Sep : ")
orig_list=user_input.split(",")
print(orig_list)
orig_list2=[]
for num in orig_list:
    orig_list2.append(int(num))
print(orig_list2)
unique_list=[]
for x in orig_list2:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)
print(f"Duplicates = {len(orig_list2)-len(unique_list)}")
