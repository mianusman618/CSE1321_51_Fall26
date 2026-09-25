total_sum=0
count=0
#for i in range(10000000000):
while True:
    user_input=int(input("Enter a num of -1 to stop : "))
    if user_input== -1:
        break
    total_sum+=user_input
    count+=1

if count>0:
    print("Total numbers entered = ",count)
    print("Avg of nums = ",total_sum/count)
else:
    print("No nums entered")
