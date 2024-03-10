
countries = ['USA', 'UK']
capitals = ['Washington DC', 'London']


# zip takes the shortest length of iterables and creates zip object only for the min of all the iterables provided to it
a = zip(countries, capitals)

print(a.__next__())
print(a.__iter__())
