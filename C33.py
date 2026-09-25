import time
count=0
while count<10:
    print(count)
    time.sleep(2)
    if count==5:
        count += 1
        continue
    print("Other line in loop")
    count+=1
print("rest of the program")