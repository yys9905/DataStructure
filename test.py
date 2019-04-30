list = []

for i in range(0, 20):
    list.append(i)
    print("List:",list)
    print("Length:",len(list))
    print("Size:",list.__sizeof__())
    print("-----------------------------")