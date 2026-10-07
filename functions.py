def myfunc1():
    print("Inside func1 in functions file")
def Sum_function(param1,param2=20):
    print(f"Param 1 = {param1} and Param 2 ={param2}")
    sum1=0

    for i in range(param1+1):
        sum1+=i
    print(f"Sum of the numbers upto {param1} = {sum1}")
    return sum1