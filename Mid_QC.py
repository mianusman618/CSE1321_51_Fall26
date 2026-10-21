def f_to_c(temp_f=0):
    Celsius = (temp_f - 32) * 5 / 9
    return Celsius
def validate_input(temp):
    if temp<-30:
        return -30
    elif temp>115:
        return 115
    else:
        return temp

input_temp=float(input("Enter a temperature: "))
validated_value=validate_input(input_temp)
cel_temp=f_to_c(validated_value)
print(f"{validated_value:.2f} F is {cel_temp:.2f} C")