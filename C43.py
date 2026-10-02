user_input=input("Enter a word : ")
for i in range(len(user_input)):
    count=1
    for j in range(i+1,len(user_input)):
        if user_input[i]==user_input[j]:
            count+=1
    print(f"Char {user_input[i]} appears {count} times")