def printHappyBirthdayImage():
    print(" ___    ___   ________   ________   ________   ____    ____")
    print("|   |  |   | |  ____  | |  ____  | |  ____  |  \   \  /   /")
    print("|   |__|   | | |    | | | |    | | | |    | |   \   \/   /")
    print("|          | | |____| | | |____| | | |____| |    \      /")
    print("|    __    | |  ____  | |  ______| |  ______|     |    |")
    print("|   |  |   | | |    | | |  |       |  |           |    |")
    print("|___|  |___| |_|    |_| |__|       |__|           |____|  ") 
    print()
    print(" __________             ____________   _________  ____    ____   __________")
    print("|  ______  |           |    ______  | |  _____  | \   \  /   /   \        /")
    print("| |      | |           |   |      | | | |     | |  \   \/   /     \      /")
    print("| |______| |   ______  |   |      | | | |_____| |   \      /       \    /")
    print("|         |   |______| |   |      | | |  _____  |    |    |         \  /")
    print("|  ______  |           |   |      | | | |     | |    |    |          \/")
    print("| |      | |           |   |      | | | |     | |    |    |          __")
    print("| |______| |           |   |______| | | |     | |    |    |         |  |")
    print("|__________|           |____________| |_|     |_|    |____|         |__|")

def singHappyBirthday(name, age):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday dear " + name + "!")
    print("Happy birthday to you!!!")
    
    for year in range(1,age):
        print("Are you " + str(year) +"?")
        
    printHappyBirthdayImage()
    

singHappyBirthday("Lauren", 24)
