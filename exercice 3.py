import random
a=random.randint(1,100)
n=0
nbressey=0
for i in range(7):
    if(n<0 or n>100):
        print(" le nomre n'est pas dans l'intervale")
    elif(n>a):
        print("plus petite")
    elif(n<a):
        print("plus grand")
    else:
        print("BRAVO")