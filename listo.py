listo = []

def listoAnd(listoIn):
    if listoIn != []:
        for item in listoIn:
            if item == listoIn[int(len(listoIn)-1)]:
                print('and ' + item)
            else:
                print(item, end=', ')
    else:
        print('Blank list!')

while True:
    listoAppend = input('Put in a value to add it to the list or press enter to send the list to the program: ')
    if listoAppend == '':
        listoAnd(listo)
        break
    else:
        listo.append(listoAppend)
        continue
