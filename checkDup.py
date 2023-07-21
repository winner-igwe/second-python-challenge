def check_duplicates(list):
    newList = []
    for i in range(len(list)):
        current_item = list[i]
        for x in range(i+1,len(list)):
            if(current_item == list[x]):
                if(not current_item in newList):
                    newList.append(current_item)

    if len(newList) > 0:
        return newList
    else:
        return "no duplicates"
