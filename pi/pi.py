import time
start = 2
wallisproduct = 1
while True:
    #time.sleep(2/start)
    wallisproduct = wallisproduct * start * start / (start-1) / (start +1)
    if start%1000000==0:
        print(wallisproduct*2)
    start += 2