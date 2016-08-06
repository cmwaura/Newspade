a = [1,2,3,None]
for items in a:
	if items is None:
		a.remove(items)
print a