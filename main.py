def countDown(x) -> int :

    for i in range(x,0,-1):
        for j in range(i,0,-1) :
            print(j,end=" ")
        print()

x = int(input("Enter a number: "))
countDown(x)