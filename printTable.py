tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    bigBoy = 0
    for outer in range(len(list)):
        for inner in range(len(list[0])):
            #print(len(list[outer][inner]))
            if len(list[outer][inner]) > bigBoy:
                bigBoy = len(list[outer][inner])
    print(bigBoy)

    for outer in range(len(list[0])):
        for inner in range(len(list[0])-1):
            print(list[inner][outer].rjust(8),end='')
        print('')


printTable(tableData)
