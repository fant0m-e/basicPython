lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers) # adds lucky numbers to friends
friends.append("Creed") # adds Creed, to the end
friends.insert(1, "Kelly") # adds Kelly before Karen (1)
# friends.remove("Jim") removes Jim
# friends.clear() empties the list completely
friends.pop() # removes or pops last element in list
# friends.sort()
# friends.reverse()
friends2 = friends.copy()


print(friends)
print(friends.index("Kevin")) # checks for Kevin - by position
print(friends.count("Jim")) # counts the Jim's
print(friends2)