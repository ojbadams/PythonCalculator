def mainMenu(): 
    res = 0 
    
    print("1: add") 
    print("2: Subtract") 
    print("3: Multiply") 
    choice = int(input("What is your input choice?"))
    num1 = int(input("Number One"))
    num2 = int(input("Number Two"))
    
    if choice == 1: 
        res = addFunc(num1,num2)
    elif choice == 2:
        res = subFunc(num1,num2)
    elif choice == 3: 
        res = multFunc(num1, num2)

    print("--------------------------")
    print("The Result is: " + str(res))
    print("--------------------------")
    
    mainMenu()


def addFunc(num1, num2):
    return num1 + num2
    
def subFunc(num1, num2):
    return num1 - num2 
    
def multFunc(num1, num2):
    return num1*num2
    
mainMenu() 