def myfunction(param1,param2=20):
    print(f"Param 1 = {param1} and Param 2 ={param2}")
    sum1=0

    for i in range(param1+1):
        sum1+=i
    print(f"Sum of the numbers upto {param1} = {sum1}")
    return sum1


func_output=myfunction(5,500)
print(f"Func Output = {func_output}")
