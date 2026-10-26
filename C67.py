user_input=input("Enter Scores Comma Seprated : ")
list_scores=user_input.split(",")
print(list_scores)
sum1=0
for e in list_scores:
    sum1+=int(e)
print("AVG =",sum1/len(list_scores))