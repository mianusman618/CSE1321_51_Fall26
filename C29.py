outer=0
inner=0
for i in range(5):
    print("Outer loop", outer)
    for j in range(3):
        print("\tInner loop",inner)
        inner+=1
        for k in range(3):
            print("inner most")
    outer += 1