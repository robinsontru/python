print("programa muestre las fichas de domino")
for i in range(0,7):
    for j in range (0,i+1):
        print("/"+str(i)+"/"+str(j) ,end="\n")