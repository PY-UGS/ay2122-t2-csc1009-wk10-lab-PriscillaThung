
def getModName(moduleCode):
    match moduleCode:
        case "CSC1006":
            return "Mathematics 2"
            
        case "CSC1007":
            return "Operating Systems"

        case "CSC1008":
            return"Data Structure and Algorithms"

        case "CSC1009":
            return "Object Orientated Programming"

        case "CSC1010":
            return "Computer Network"
        
        case _:
            return "unknown"


def forLoop():
    for i in range(102, 66, -1):
        if(i%2 ==1):
            print("value of i: " + str(i))
    return

modName = input("Enter module code: ")
print(getModName(modName))
forLoop()

