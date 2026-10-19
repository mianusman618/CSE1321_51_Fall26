limit=int(input("Enter the maximum integer limit: "))

print("Generating script...\n")
print("Copy from the line below: ")
print()

for i in range(1,limit+1):
    for j in range(1,limit+1):
        if i==1 and j==1:
            print(f"if num1 == {i} and num2 == {j}:")
            print(f"\tprint({i+j})")
        else:
            print(f"elif num1 == {i} and num2 == {j}:")
            print(f"\tprint({i + j})")

print(f"else:")
print(f"\tprint('I cannot do addition with such large numbers')")