def func1():
    var1=50
    var2="ABC"
    var3=6.8
    return var1,var2,var3

fun_output=func1()
print(fun_output)
out1,_,out3=func1()
print(f"out1 {out1}")
print(f"out3 {out3}")