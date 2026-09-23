count=0
while count<10:
    print(count,end=" , ")
    count += 1
    if count==5:
        print("Its at 5")
        continue

print("rest of the program")