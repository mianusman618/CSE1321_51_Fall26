import time as t
seconds=t.time()
print(seconds)
print(t.ctime(seconds))

for i in range(10,0,-1):
    print(i)
    t.sleep(2)