# may contain elements of different types
dataList = ["Kevin", 2, True]
print(dataList)
print(dataList[0], dataList[1], dataList[2])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
# referral by index (starts with 0)
print(friends[0] + "\n" + friends[1] + "\n" + friends[2])
# negative index values count from the end of the list
print(friends[-1])
# several index values
# from position 1 until the last element of the list
print(friends[1:])
# from position 1 to the element ar position 3 (not included)
print(friends[1:3])
# modify elements by index
friends[1] = "Mike"
print(friends)
