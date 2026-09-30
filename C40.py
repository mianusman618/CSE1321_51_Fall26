user_input=int(input("Enter a num to see its factorial : "))# 3----0*3*2*1....5---0*5*4*3*2*1
fact=1
while user_input >= 1:
    fact=fact*user_input # 0=0*3--- 0 --- 0=0*2=0--0=0*1=0
    user_input-=1#3--2--- 2--1....1--0
print("Factorial is = ",fact)