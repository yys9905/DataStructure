def find(L, target, start, end):
    if start > end:
        return -1
    midNum =(start + end) // 2
    if L[midNum] == target:
        return midNum
    elif L[midNum] < target:
        return find(L, target, midNum + 1, end)
    elif L[midNum] > target:
        return find(L, target, start, midNum - 1)



L = []
L.append(5)
L.append(8)
L.append(10)
L.append(15)
L.append(20)
L.append(25)
L.append(30)
L.append(40)
L.append(50)
L.append(54)
L.append(66)
L.append(69)
L.append(83)
L.append(86)
L.append(90)

index = find(L, 67, 0, len(L)-1) #(리스트,찾고싶은 값, 시작index, 마지막index)
print(index)