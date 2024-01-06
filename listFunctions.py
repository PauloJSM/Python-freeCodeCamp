lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

# concatenates a new list to the initial one
friends.extend(lucky_numbers)
print(friends)

# appends a single element to the list
friends.append(lucky_numbers[1])
print(friends)
friends.append("Creed")
print(friends)

# inserts a specific element at a specific position of the list
friends.insert(1, "Kelly")
print(friends)
friends.insert(0, lucky_numbers[3])
print(friends)

# removing elements
friends.remove("Jim")
print(friends)
friends.remove(friends[0])
print(friends)

# remove all elements
lucky_numbers.clear()
print(lucky_numbers)

# remove last element from the list
friends.pop()
print(friends)

# if it's argument belongs to the list, returns it's index
print(friends.index("Kevin"))

# counts the number of occurrences
print(friends.count("Jim"))
print(friends.count("Kelly"))

# sorts the list in ascending order
friends = ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby']
print(friends)
friends.sort()
print(friends)

# sorts the list in descending order
friends.reverse()
print(friends)

# copy
friends2 = friends.copy()
print(friends)
print(friends2)

friends3 = friends2
print(friends3)
