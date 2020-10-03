thistuple = ("apple , banana")
# convert to list
listtuple = list(thistuple)
# update the list value
listtuple.insert(1, 'berries')
# update the list to a tuple
thistuple = tuple(listtuple)
print(thistuple)
