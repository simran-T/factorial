x = int(input("Enter the positive integer: "))
for i in range(1,x+1):
    if x%i == 0:
        print(i , "is a factor of" , x)
       