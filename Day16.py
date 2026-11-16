# Match Case Statement... 



A = int(input("Enter the value of A : "))
print("The value of X is :", A)

match A:
    case 0:
        print("A is 0")
    case 1:
        print("Case is 1")
        
    case _ if A != 90:
        print(A, "is not 90")
    case _ if A == 80:
        print(A, "is 80")
    case _:
        print(A)
            