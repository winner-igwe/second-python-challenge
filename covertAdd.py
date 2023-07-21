
def convert_add (list):
    newList = []
    num = 0
    for i in range(len(list)):
        newList.append(int(list[i]))
    for i in range(len(newList)):
        num += newList[i]

    return num
