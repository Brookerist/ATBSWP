def collatz(userNum):

    if userNum % 2 == 0:
        userNum = userNum // 2
        print(userNum)
        return userNum
    elif userNum % 2 == 1:
        userNum = 3 * userNum + 1
        print(userNum)
        return userNum


while True:
    print("Enter a number")
    try:
        userNum = int(input())
        while userNum:
            if userNum != 1:
                userNum = collatz(userNum)
                continue
            elif userNum == 1:
                break
    except ValueError:
        print("Not a number.")
